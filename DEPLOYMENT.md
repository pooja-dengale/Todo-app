# Django ToDo App - Deployment Guide

## Prerequisites
- Python 3.11+
- Git installed
- Account on deployment platform (Heroku, Railway, Render, or PythonAnywhere)

## Local Setup

1. **Create virtual environment:**
```bash
cd dist
python -m venv venv
```

2. **Activate virtual environment:**
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

3. **Install dependencies:**
```bash
pip install -r requirements.txt
```

4. **Create .env file:**
```bash
cp .env.example .env
```

5. **Generate a new SECRET_KEY:**
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
Copy the output and paste it in your `.env` file.

6. **Run migrations:**
```bash
python manage.py migrate
```

7. **Create superuser:**
```bash
python manage.py createsuperuser
```

8. **Collect static files:**
```bash
python manage.py collectstatic --noinput
```

9. **Test locally:**
```bash
python manage.py runserver
```

---

## Deployment Options

### Option 1: Heroku

1. **Install Heroku CLI** from https://devcenter.heroku.com/articles/heroku-cli

2. **Login to Heroku:**
```bash
heroku login
```

3. **Create Heroku app:**
```bash
heroku create your-app-name
```

4. **Set environment variables:**
```bash
heroku config:set SECRET_KEY="your-secret-key-here"
heroku config:set DEBUG=False
heroku config:set ALLOWED_HOSTS="your-app-name.herokuapp.com"
```

5. **Deploy:**
```bash
git init
git add .
git commit -m "Initial commit"
git push heroku main
```

6. **Run migrations:**
```bash
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
```

7. **Open app:**
```bash
heroku open
```

---

### Option 2: Railway

1. **Install Railway CLI** or use web interface at https://railway.app

2. **Login:**
```bash
railway login
```

3. **Initialize project:**
```bash
railway init
```

4. **Add environment variables in Railway dashboard:**
- SECRET_KEY
- DEBUG=False
- ALLOWED_HOSTS=your-domain.railway.app

5. **Deploy:**
```bash
railway up
```

6. **Run migrations:**
```bash
railway run python manage.py migrate
railway run python manage.py createsuperuser
```

---

### Option 3: Render

1. **Create account at** https://render.com

2. **Push code to GitHub**

3. **Create new Web Service:**
   - Connect your GitHub repository
   - Build Command: `./build.sh`
   - Start Command: `gunicorn dist.wsgi:application`

4. **Add environment variables in Render dashboard:**
   - SECRET_KEY (use Generate button)
   - DEBUG=False
   - DATABASE_URL (from PostgreSQL service)
   - RENDER_EXTERNAL_HOSTNAME=your-app.onrender.com
   - PYTHON_VERSION=3.11.0

5. **Create PostgreSQL Database:**
   - Click "New +" → "PostgreSQL"
   - Connect to your web service

6. **Deploy automatically on git push**

For detailed Render deployment instructions, see [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)

---

### Option 4: PythonAnywhere

1. **Create account at** https://www.pythonanywhere.com

2. **Upload your code:**
- Use Git or upload files directly

3. **Create virtual environment:**
```bash
mkvirtualenv --python=/usr/bin/python3.11 myenv
pip install -r requirements.txt
```

4. **Configure WSGI file:**
- Edit `/var/www/yourusername_pythonanywhere_com_wsgi.py`
- Point to your Django project

5. **Set environment variables:**
- Add to WSGI file or use .env

6. **Run migrations:**
```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py collectstatic
```

7. **Reload web app**

---

## Post-Deployment Checklist

- [ ] SECRET_KEY is set and different from development
- [ ] DEBUG is set to False
- [ ] ALLOWED_HOSTS includes your domain
- [ ] Database migrations are run
- [ ] Superuser account is created
- [ ] Static files are collected
- [ ] HTTPS is enabled
- [ ] Test user registration
- [ ] Test login/logout
- [ ] Test task CRUD operations

---

## Troubleshooting

**Static files not loading:**
```bash
python manage.py collectstatic --noinput
```

**Database errors:**
```bash
python manage.py migrate
```

**500 errors:**
- Check logs: `heroku logs --tail` (Heroku)
- Ensure DEBUG=False
- Check ALLOWED_HOSTS

**CSRF errors:**
- Add your domain to ALLOWED_HOSTS
- Ensure CSRF_COOKIE_SECURE is set correctly

---

## Maintenance

**Update dependencies:**
```bash
pip install --upgrade -r requirements.txt
```

**Backup database:**
```bash
python manage.py dumpdata > backup.json
```

**Restore database:**
```bash
python manage.py loaddata backup.json
```

---

## Support

For issues, check:
- Django documentation: https://docs.djangoproject.com
- Platform-specific docs (Heroku, Railway, Render, PythonAnywhere)
