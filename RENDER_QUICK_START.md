# Deploy to Render - Quick Start Guide

Follow these simple steps to deploy your Django todo app to Render.

## Prerequisites

- [ ] GitHub account (create at https://github.com if you don't have one)
- [ ] Render account (sign up free at https://render.com)
- [ ] Your code ready to push

---

## Step 1: Push Your Code to GitHub

### 1.1 Create a GitHub Repository

1. Go to https://github.com
2. Click the "+" icon (top right) → "New repository"
3. Name it: `django-todo-app`
4. Keep it Public or Private (your choice)
5. Don't add README, .gitignore, or license (we already have them)
6. Click "Create repository"

### 1.2 Push Your Code

Open your terminal in the `dist` folder and run:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Production-ready Django todo app"

# Add your GitHub repository as remote
# Replace YOUR_USERNAME with your GitHub username
git remote add origin https://github.com/YOUR_USERNAME/django-todo-app.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Enter your GitHub username and password (or personal access token) when prompted.**

✅ Your code is now on GitHub!

---

## Step 2: Deploy on Render

### 2.1 Sign Up / Log In to Render

1. Go to https://render.com
2. Click "Get Started for Free"
3. Sign up with GitHub (recommended) or email
4. Verify your email if needed

### 2.2 Create New Web Service Using Blueprint

1. In Render Dashboard, click **"New +"** (top right)
2. Select **"Blueprint"**
3. Click **"Connect GitHub"** (if not already connected)
4. Authorize Render to access your GitHub repositories
5. Find and select your `django-todo-app` repository
6. Click **"Connect"**

### 2.3 Review and Deploy

Render will automatically detect your `render.yaml` file and show:

- **Web Service**: django-todo-app
- **Database**: django-todo-db (PostgreSQL)

**Configuration Preview:**
- Build Command: `./build.sh`
- Start Command: `gunicorn dist.wsgi:application`
- Python Version: 3.11.0
- Environment Variables: Auto-generated

Click **"Apply"** to start deployment.

### 2.4 Wait for Deployment

You'll see the build logs in real-time:

```
==> Installing dependencies...
==> Running collectstatic...
==> Running migrations...
==> Build successful!
==> Starting service...
```

**First deployment takes 5-10 minutes.** ⏱️

✅ Your app is now live!

---

## Step 3: Create Admin User

After deployment completes:

1. Go to your web service in Render Dashboard
2. Click the **"Shell"** tab (top menu)
3. Wait for shell to connect
4. Run this command:

```bash
python manage.py createsuperuser
```

5. Enter:
   - Username: `admin` (or your choice)
   - Email: your email
   - Password: create a strong password
   - Confirm password

✅ Admin user created!

---

## Step 4: Access Your Application

Your app is now live! Find your URL in the Render Dashboard (top of the page).

It will look like: `https://django-todo-app-xxxx.onrender.com`

### Test These URLs:

1. **Main App**: `https://your-app-name.onrender.com`
   - Should show the login page

2. **Health Check**: `https://your-app-name.onrender.com/health/`
   - Should return: `{"status": "healthy", "service": "django-todo-app"}`

3. **Admin Panel**: `https://your-app-name.onrender.com/admin`
   - Login with the superuser you created

### Test the App:

1. Click "Register" and create a test user
2. Login with your new user
3. Create a task
4. Test search and filter
5. Edit and delete tasks

✅ Everything should work!

---

## Step 5: Automatic Deployments

Every time you push to GitHub, Render automatically redeploys:

```bash
# Make changes to your code
git add .
git commit -m "Add new feature"
git push origin main
```

Render will detect the push and redeploy automatically! 🚀

---

## Common Issues & Solutions

### Issue 1: Build Fails

**Error**: `Permission denied: ./build.sh`

**Solution**: Make build.sh executable before pushing:
```bash
git update-index --chmod=+x build.sh
git commit -m "Make build.sh executable"
git push
```

### Issue 2: Static Files Not Loading

**Check**:
1. Go to Render Dashboard → Logs
2. Look for "collectstatic" in build logs
3. Should see: "X static files copied"

**Solution**: Already configured in `build.sh`

### Issue 3: Database Connection Error

**Check**:
1. Render Dashboard → PostgreSQL service
2. Verify it's "Available"
3. Check DATABASE_URL is connected to web service

**Solution**: Render auto-connects this via `render.yaml`

### Issue 4: App Spins Down (Free Tier)

**Behavior**: First request after 15 minutes takes 30-60 seconds

**This is normal on free tier!** Upgrade to paid plan ($7/month) to prevent spin-down.

### Issue 5: CSRF Error

**Error**: "CSRF verification failed"

**Solution**: Already configured! CSRF_TRUSTED_ORIGINS includes your Render domain.

---

## View Logs

To debug issues:

1. Render Dashboard → Your Web Service
2. Click **"Logs"** tab
3. View real-time logs
4. Look for errors in red

---

## Environment Variables

Render automatically sets these (from `render.yaml`):

| Variable | Value |
|----------|-------|
| SECRET_KEY | Auto-generated (secure) |
| DEBUG | False |
| DATABASE_URL | Auto-connected |
| RENDER_EXTERNAL_HOSTNAME | your-app.onrender.com |
| PYTHON_VERSION | 3.11.0 |
| WEB_CONCURRENCY | 4 |

**You don't need to set these manually!** ✅

---

## Upgrade to Paid Plan (Optional)

Free tier limitations:
- App spins down after 15 minutes of inactivity
- 750 hours/month (enough for one service)
- 1GB PostgreSQL storage

Paid plan benefits ($7/month per service):
- No spin-down (always fast)
- More resources
- Automatic backups
- Custom domains

To upgrade:
1. Render Dashboard → Your Service
2. Click "Upgrade" button
3. Choose "Starter" plan ($7/month)

---

## Custom Domain (Optional)

To use your own domain:

1. Render Dashboard → Your Web Service
2. Click "Settings" → "Custom Domain"
3. Add your domain (e.g., `todo.yourdomain.com`)
4. Update your DNS records as instructed
5. SSL certificate auto-generated (free!)

---

## Monitoring Your App

### Check Health
```bash
curl https://your-app-name.onrender.com/health/
```

Should return:
```json
{"status": "healthy", "service": "django-todo-app"}
```

### View Metrics
1. Render Dashboard → Your Service
2. Click "Metrics" tab
3. View CPU, Memory, Request metrics

### Set Up Alerts
1. Render Dashboard → Your Service
2. Click "Settings" → "Notifications"
3. Add email or Slack webhook

---

## Backup Your Database

### Manual Backup (Free Tier)

1. Render Dashboard → PostgreSQL service
2. Click "Shell" tab
3. Run:
```bash
pg_dump $DATABASE_URL > backup.sql
```

### Automatic Backups (Paid Plans)

1. Upgrade PostgreSQL to paid plan ($7/month)
2. Automatic daily backups included
3. Point-in-time recovery available

---

## Summary

You've successfully deployed your Django todo app! 🎉

**Your app is now:**
- ✅ Live on the internet
- ✅ Using PostgreSQL database
- ✅ Secured with HTTPS
- ✅ Auto-deploying on git push
- ✅ Production-ready

**Next steps:**
1. Share your app URL with friends
2. Add more features
3. Push to GitHub to auto-deploy
4. Consider upgrading for better performance

---

## Quick Reference

### Your URLs
- App: `https://your-app-name.onrender.com`
- Admin: `https://your-app-name.onrender.com/admin`
- Health: `https://your-app-name.onrender.com/health/`

### Useful Commands
```bash
# Push updates
git add .
git commit -m "Update"
git push

# View logs
# Go to Render Dashboard → Logs

# Create superuser
# Go to Render Dashboard → Shell
python manage.py createsuperuser
```

### Support
- Render Docs: https://render.com/docs
- Render Community: https://community.render.com
- Django Docs: https://docs.djangoproject.com

---

**Need help?** Check the detailed guide: [RENDER_DEPLOYMENT.md](RENDER_DEPLOYMENT.md)

**Congratulations on your deployment!** 🚀
