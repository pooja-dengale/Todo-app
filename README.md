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
- ✅ Task priority levels (Low, Medium, High)
- ✅ Due date tracking
- ✅ Search functionality (title and description)
- ✅ Filter by status (All, Pending, Completed)
- ✅ Pagination (10 tasks per page)
- ✅ Modern, responsive UI with purple gradient theme
- ✅ Secure delete confirmation
- ✅ Comprehensive test suite
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

## Quick Start

### Local Development

1. Clone and setup:
```bash
cd dist
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure environment:
```bash
cp .env.example .env
# Edit .env and add your SECRET_KEY
```

3. Run migrations and start:
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Deploy to Render (Production)

**🚨 IMPORTANT**: You got an error? See [QUICK_FIX.md](QUICK_FIX.md) for the solution!

**Simple 3-Step Process:**

1. **Push to GitHub** - Upload your code (from inside the `dist` folder!)
2. **Connect to Render** - Link your repository  
3. **Deploy** - Render does everything automatically!

📖 **Step-by-step guide**: [RENDER_QUICK_START.md](RENDER_QUICK_START.md) ← Start here!

🔧 **Got "No module named 'app'" error?**: [QUICK_FIX.md](QUICK_FIX.md) ← Fix it here!

📚 **Detailed documentation**: [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)

## Usage

### User Registration
1. Navigate to `/register/`
2. Fill in username, email, and password
3. Click "Register" to create account
4. You'll be automatically logged in

### Managing Tasks
1. **Create Task:** Click "+ Add Task" button, set title, description, priority, and optional due date
2. **Edit Task:** Click "Edit" button on any task
3. **Delete Task:** Click "Delete" button and confirm
4. **Mark Complete:** Edit task and check "Completed" checkbox
5. **Search Tasks:** Use the search bar to find tasks by title or description
6. **Filter Tasks:** Use the status dropdown to filter by Pending or Completed tasks
7. **Navigate Pages:** Use pagination controls when you have more than 10 tasks

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

This application is production-ready and can be deployed to various platforms.

### Quick Deploy to Render (Recommended)

1. Push your code to GitHub
2. Go to [Render Dashboard](https://dashboard.render.com)
3. Click "New +" → "Blueprint"
4. Connect your repository
5. Render will auto-detect `render.yaml` and deploy everything

See [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md) for detailed instructions.

### Other Platforms

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

## Testing

Run the test suite:
```bash
python manage.py test
```

Run tests with coverage:
```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
```

## Future Enhancements

- [ ] Task categories/tags
- [ ] Email reminders for due dates
- [ ] Task sharing between users
- [ ] REST API for mobile apps
- [ ] Dark mode toggle
- [ ] Email notifications
- [ ] Task attachments
- [ ] Recurring tasks

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
