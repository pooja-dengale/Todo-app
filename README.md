# Django ToDo Application

A full-featured ToDo application built with Django 5, featuring user authentication, task management, and a modern purple gradient UI.

![Django](https://img.shields.io/badge/Django-5.0.1-green.svg)
![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

- ✅ User Registration & Authentication
- ✅ Create, Read, Update, Delete Tasks
- ✅ User-specific task management
- ✅ Task completion status tracking
- ✅ Modern, responsive UI with purple gradient theme
- ✅ Secure delete confirmation
- ✅ Production-ready configuration

## Screenshots

### Login Page
Clean authentication interface with purple gradient background.

### Task List
View all your tasks with status badges and action buttons.

### Task Form
Create and edit tasks with a simple, intuitive form.

## Tech Stack

- **Backend:** Django 5.0.1
- **Database:** SQLite (development) / PostgreSQL (production ready)
- **Frontend:** HTML5, CSS3 (Custom styling)
- **Deployment:** Gunicorn, WhiteNoise
- **Security:** CSRF protection, user authentication, secure sessions

## Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Git

### Local Setup

1. **Clone the repository:**
```bash
git clone https://github.com/yourusername/django-todo-app.git
cd django-todo-app/dist
```

2. **Create virtual environment:**
```bash
python -m venv venv
```

3. **Activate virtual environment:**
- Windows:
  ```bash
  venv\Scripts\activate
  ```
- Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Create .env file:**
```bash
cp .env.example .env
```

6. **Generate SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copy the output and add it to your `.env` file:
```
SECRET_KEY=your-generated-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

7. **Run migrations:**
```bash
python manage.py migrate
```

8. **Create superuser (admin):**
```bash
python manage.py createsuperuser
```

9. **Run development server:**
```bash
python manage.py runserver
```

10. **Open in browser:**
```
http://127.0.0.1:8000/
```

## Usage

### User Registration
1. Navigate to `/register/`
2. Fill in username, email, and password
3. Click "Register" to create account
4. You'll be automatically logged in

### Managing Tasks
1. **Create Task:** Click "+ Add Task" button
2. **Edit Task:** Click "Edit" button on any task
3. **Delete Task:** Click "Delete" button and confirm
4. **Mark Complete:** Edit task and check "Completed" checkbox

### Admin Panel
Access the admin panel at `/admin/` with your superuser credentials to manage users and tasks.

## Project Structure

```
dist/
├── dist/                   # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Main URL configuration
│   └── wsgi.py            # WSGI configuration
├── todo/                   # Todo app
│   ├── migrations/        # Database migrations
│   ├── static/            # Static files (CSS)
│   ├── templates/         # HTML templates
│   ├── models.py          # Task model
│   ├── views.py           # View functions
│   ├── forms.py           # Forms (Task, Register)
│   └── urls.py            # App URL configuration
├── templates/             # Base templates
├── manage.py              # Django management script
├── requirements.txt       # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore rules
├── Procfile               # Deployment configuration
└── README.md              # This file
```

## Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions for:
- Heroku
- Railway
- Render
- PythonAnywhere

## Security Features

- User authentication required for all task operations
- CSRF protection on all forms
- User-specific task isolation (users can only see/edit their own tasks)
- Secure password hashing
- Production security settings (HTTPS, secure cookies)
- SQL injection protection via Django ORM

## API Endpoints

| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/` | GET | Task list | Yes |
| `/create/` | GET/POST | Create task | Yes |
| `/update/<id>/` | GET/POST | Update task | Yes |
| `/delete/<id>/` | GET/POST | Delete task | Yes |
| `/register/` | GET/POST | User registration | No |
| `/login/` | GET/POST | User login | No |
| `/logout/` | POST | User logout | Yes |
| `/admin/` | GET | Admin panel | Admin only |

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Enhancements

- [ ] Task categories/tags
- [ ] Due dates and reminders
- [ ] Task priority levels
- [ ] Search and filter functionality
- [ ] Task sharing between users
- [ ] REST API for mobile apps
- [ ] Dark mode toggle
- [ ] Email notifications

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Your Name - [Your GitHub Profile](https://github.com/yourusername)

## Acknowledgments

- Django documentation
- Django community
- Bootstrap inspiration for UI patterns

## Support

If you found this project helpful, please give it a ⭐️!

For issues and questions, please open an issue on GitHub.
