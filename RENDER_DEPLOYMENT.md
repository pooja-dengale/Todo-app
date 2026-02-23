# Deploy Django Todo App to Render

This guide will help you deploy your Django todo application to Render.com with PostgreSQL database.

## Prerequisites

- GitHub account
- Render account (free tier available at https://render.com)
- Your code pushed to a GitHub repository

## Deployment Steps

### Option 1: Using render.yaml (Recommended - Infrastructure as Code)

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for Render deployment"
   git push origin main
   ```

2. **Create a new Web Service on Render**
   - Go to https://dashboard.render.com
   - Click "New +" and select "Blueprint"
   - Connect your GitHub repository
   - Render will automatically detect `render.yaml` and create:
     - Web Service (Django app)
     - PostgreSQL Database

3. **Configure Environment Variables**
   
   Render will auto-generate most variables, but verify these in your dashboard:
   
   - `SECRET_KEY` - Auto-generated (keep it secret!)
   - `DEBUG` - Set to `False`
   - `DATABASE_URL` - Auto-connected from PostgreSQL service
   - `RENDER_EXTERNAL_HOSTNAME` - Auto-set to your app URL
   - `PYTHON_VERSION` - Set to `3.11.0`

4. **Deploy**
   - Click "Apply" to start deployment
   - Wait for build to complete (5-10 minutes first time)
   - Your app will be live at `https://your-app-name.onrender.com`

### Option 2: Manual Setup

1. **Create PostgreSQL Database**
   - Go to Render Dashboard
   - Click "New +" → "PostgreSQL"
   - Name: `django-todo-db`
   - Database: `todo_db`
   - User: `todo_user`
   - Region: Choose closest to you
   - Plan: Free
   - Click "Create Database"
   - Copy the "Internal Database URL"

2. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - Name: `django-todo-app`
     - Region: Same as database
     - Branch: `main`
     - Root Directory: `dist` (if your Django app is in dist folder)
     - Runtime: `Python 3`
     - Build Command: `./build.sh`
     - Start Command: `gunicorn dist.wsgi:application`
     - Plan: Free

3. **Add Environment Variables**
   
   In the "Environment" section, add:
   
   ```
   SECRET_KEY=<click "Generate" button>
   DEBUG=False
   DATABASE_URL=<paste Internal Database URL from step 1>
   PYTHON_VERSION=3.11.0
   WEB_CONCURRENCY=4
   ```

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically deploy your app
   - First deployment takes 5-10 minutes

## Post-Deployment Steps

### 1. Create Superuser

After successful deployment, create an admin user:

```bash
# In Render Dashboard, go to your web service
# Click "Shell" tab
# Run:
python manage.py createsuperuser
```

Follow the prompts to create your admin account.

### 2. Access Your Application

- Main app: `https://your-app-name.onrender.com`
- Admin panel: `https://your-app-name.onrender.com/admin`

### 3. Test the Application

1. Register a new user
2. Create some tasks
3. Test search and filter functionality
4. Verify pagination works
5. Test task CRUD operations

## Automatic Deployments

Render automatically deploys when you push to your main branch:

```bash
git add .
git commit -m "Update feature"
git push origin main
```

Render will detect the push and redeploy automatically.

## Monitoring & Logs

### View Logs
- Go to your web service in Render Dashboard
- Click "Logs" tab
- View real-time application logs

### Monitor Performance
- Click "Metrics" tab
- View CPU, Memory, and Request metrics

## Database Management

### Backup Database
```bash
# In Render Dashboard → PostgreSQL service
# Click "Backups" tab
# Manual backups available on paid plans
```

### Connect to Database
```bash
# Get connection string from Render Dashboard
# Use psql or any PostgreSQL client
psql <EXTERNAL_DATABASE_URL>
```

## Troubleshooting

### Build Fails

**Issue**: Build script fails
```bash
# Check build.sh has execute permissions
chmod +x build.sh
git add build.sh
git commit -m "Fix build script permissions"
git push
```

**Issue**: Missing dependencies
```bash
# Verify requirements.txt includes all packages
pip freeze > requirements.txt
```

### Application Errors

**Issue**: 500 Internal Server Error
- Check logs in Render Dashboard
- Verify all environment variables are set
- Ensure `DEBUG=False` in production

**Issue**: Static files not loading
```bash
# Verify build.sh runs collectstatic
# Check STATIC_ROOT and STATIC_URL in settings.py
```

**Issue**: Database connection errors
- Verify DATABASE_URL is set correctly
- Check PostgreSQL service is running
- Ensure migrations ran successfully

### CSRF Errors

**Issue**: CSRF verification failed
```python
# In settings.py, verify:
CSRF_TRUSTED_ORIGINS = [
    'https://your-app-name.onrender.com',
]
```

## Performance Optimization

### Free Tier Limitations
- App spins down after 15 minutes of inactivity
- First request after spin-down takes 30-60 seconds
- 750 hours/month free (enough for one service)

### Upgrade to Paid Plan
- No spin-down
- More CPU and RAM
- Custom domains
- Automatic backups
- Starting at $7/month

## Custom Domain

1. Go to your web service settings
2. Click "Custom Domain"
3. Add your domain
4. Update DNS records as instructed
5. SSL certificate auto-generated

## Environment Variables Reference

| Variable | Description | Example |
|----------|-------------|---------|
| SECRET_KEY | Django secret key | Auto-generated |
| DEBUG | Debug mode | False |
| DATABASE_URL | PostgreSQL connection | Auto-connected |
| ALLOWED_HOSTS | Allowed domains | your-app.onrender.com |
| RENDER_EXTERNAL_HOSTNAME | Render hostname | your-app.onrender.com |
| PYTHON_VERSION | Python version | 3.11.0 |
| WEB_CONCURRENCY | Gunicorn workers | 4 |

## Security Checklist

- [x] DEBUG=False in production
- [x] SECRET_KEY is unique and secret
- [x] ALLOWED_HOSTS configured
- [x] HTTPS enforced
- [x] CSRF protection enabled
- [x] Secure cookies enabled
- [x] HSTS headers set
- [x] Database uses SSL
- [x] Static files served via WhiteNoise

## Cost Estimate

### Free Tier
- Web Service: Free (with limitations)
- PostgreSQL: Free (1GB storage)
- Total: $0/month

### Starter Tier
- Web Service: $7/month
- PostgreSQL: $7/month
- Total: $14/month

## Support

- Render Documentation: https://render.com/docs
- Render Community: https://community.render.com
- Django Documentation: https://docs.djangoproject.com

## Next Steps

1. Set up monitoring and alerts
2. Configure custom domain
3. Set up automated backups
4. Add email notifications
5. Implement caching (Redis)
6. Add CI/CD pipeline

---

**Congratulations!** Your Django Todo app is now live on Render! 🎉
