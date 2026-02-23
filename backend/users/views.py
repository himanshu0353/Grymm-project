from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta
from rest_framework_simplejwt.tokens import RefreshToken
from .models import OTP
from .utils import generate_otp, send_otp_email
from .permissions import IsAdmin

User = get_user_model()

OTP_EXPIRY_MINUTES = 5


class SendOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response(
                {'error': 'Email is required'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        otp = generate_otp()
        OTP.objects.create(email=email, otp=otp)

        try:
            send_otp_email(email, otp)
        except Exception as e:
            print(f"Error sending email: {e}")
            return Response(
                {'error': str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        return Response({'message': 'OTP sent'}, status=status.HTTP_200_OK)


class VerifyOTPView(APIView):
    def post(self, request):
        email = request.data.get('email')
        otp = request.data.get('otp')

        if not email or not otp:
            return Response(
                {'error': 'Email and OTP are required'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        otp_obj = OTP.objects.filter(email=email, otp=otp, is_used=False).last()

        if not otp_obj:
            return Response(
                {'error': 'Invalid OTP'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Enforce OTP expiry (5-minute window)
        expiry_time = otp_obj.created_at + timedelta(minutes=OTP_EXPIRY_MINUTES)
        if timezone.now() > expiry_time:
            otp_obj.is_used = True
            otp_obj.save()
            return Response(
                {'error': 'OTP has expired. Please request a new one.'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        otp_obj.is_used = True
        otp_obj.save()

        # Auto-create customers only; barbers/admins are pre-created by admin
        user, created = User.objects.get_or_create(
            email=email,
            defaults={'role': User.ROLE_CUSTOMER},
        )

        refresh = RefreshToken.for_user(user)

        return Response({
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            'role': user.role,
        }, status=status.HTTP_200_OK)


class CreateBarberView(APIView):
    """Admin-only endpoint to create barber accounts."""
    permission_classes = [IsAuthenticated, IsAdmin]

    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response(
                {'error': 'Email is required'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {'error': 'A user with this email already exists'},
                status=status.HTTP_400_BAD_REQUEST,
            )

        User.objects.create_user(email=email, role=User.ROLE_BARBER)

        return Response({
            'message': 'Barber account created successfully',
            'email': email,
            'role': User.ROLE_BARBER,
        }, status=status.HTTP_201_CREATED)
