# Grymm - Barber Management System

A complete barber shop management solution with separate frontend (Flutter) and backend (Django) APIs.

## Project Structure

```
Grymm/
├── frontend/          # Flutter Mobile & Web Application
│   ├── lib/          # Dart source code
│   ├── android/      # Android platform files
│   ├── ios/          # iOS platform files
│   ├── web/          # Web platform files
│   ├── pubspec.yaml  # Flutter dependencies
│   └── README.md     # Frontend setup guide
│
├── backend/           # Django REST API
│   ├── grymm_backend/ # Django project settings
│   ├── users/        # User management app
│   ├── manage.py     # Django management
│   ├── db.sqlite3    # Database
│   └── README.md     # Backend setup guide
│
├── .venv/            # Python virtual environment (shared)
├── .gitignore        # Git ignore rules
└── README.md         # This file
```

## Quick Start

### Prerequisites
- Flutter SDK (3.0+)
- Python 3.8+
- Node.js (optional, for web development)

### Backend Setup

1. **Navigate to backend folder**
   ```bash
   cd backend
   ```

2. **Activate virtual environment** (from project root)
   ```bash
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```
   Server runs on `http://127.0.0.1:8000`

### Frontend Setup

1. **Navigate to frontend folder**
   ```bash
   cd frontend
   ```

2. **Get Flutter dependencies**
   ```bash
   flutter pub get
   ```

3. **Run on web**
   ```bash
   flutter run -d chrome
   ```

4. **Run on Android**
   ```bash
   flutter run -d android
   ```

5. **Run on iOS**
   ```bash
   flutter run -d ios
   ```

## Features

### Barber Side
- Dashboard with statistics
- Appointment management (Today, Upcoming, Completed)
- Manage service slots
- Manage services offered
- Profile management

### Customer Side (Coming Soon)
- Browse available services
- Book appointments
- Manage bookings
- History and ratings
- Profile management

## API Documentation

See [backend/README.md](backend/README.md) for detailed API endpoints and authentication.

## Technology Stack

- **Frontend:** Flutter (Dart)
- **Backend:** Django (Python)
- **Database:** SQLite (Development), PostgreSQL (Production)
- **API:** REST API with JWT Authentication

## Development Guidelines

### Code Structure
- Each feature should be self-contained
- Follow the existing folder structure
- Use meaningful commit messages

### Frontend
- Keep UI components reusable
- Follow Material Design guidelines
- Use proper state management

### Backend
- Separate concerns using Django apps
- Use Django REST Framework
- Include proper error handling

## Configuration

### CORS Setup
The backend is configured to accept requests from `http://127.0.0.1` (web and mobile).

Update `backend/grymm_backend/settings.py` for production URLs.

### Environment Variables
Create a `.env` file in the backend folder:
```
DEBUG=True
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1
```

## Testing

### Frontend
```bash
cd frontend
flutter test
```

### Backend
```bash
cd backend
python manage.py test
```

## Deployment

See individual README files in `frontend/` and `backend/` folders for deployment instructions.

## Contributing

1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## License

MIT License - See LICENSE file for details

## Contact

For questions or issues, please create an issue in the repository.

---

**Last Updated:** February 19, 2026
