# 🚨 FIX THE ERROR NOW - 2 Minutes

## The Problem
Render is running: `gunicorn app.wsgi:application`  
But it should run: `gunicorn dist.wsgi:application`

## The Fix (Do This Right Now)

### Step 1: Go to Render Dashboard
1. Open: https://dashboard.render.com
2. Click on your **django-todo-app** service

### Step 2: Update Start Command
1. Click **"Settings"** in the left sidebar
2. Scroll down to **"Start Command"**
3. You'll see it says: `gunicorn app.wsgi:application`
4. Change it to: **`gunicorn dist.wsgi:application`**
5. Click **"Save Changes"**

### Step 3: Set Root Directory
1. Still in Settings, scroll to **"Root Directory"**
2. Set it to: **`dist`**
3. Click **"Save Changes"**

### Step 4: Redeploy
1. Click **"Manual Deploy"** button (top right)
2. Click **"Deploy latest commit"**
3. Wait 5-10 minutes

## That's It!

Watch the logs. You should see:
```
==> Build successful 🎉
==> Deploying...
==> Running 'gunicorn dist.wsgi:application'
[INFO] Booting worker with pid: 123
```

## Test After Deployment

Visit: `https://your-app-name.onrender.com/health/`

Should return:
```json
{"status": "healthy", "service": "django-todo-app"}
```

---

## If You Still Get Errors

### Alternative: Delete and Recreate Service

If the above doesn't work, you might need to recreate the service:

1. **Delete the old service**:
   - Render Dashboard → Your Service
   - Settings → Scroll to bottom
   - Click "Delete Web Service"

2. **Create new service using Blueprint**:
   - Dashboard → "New +" → "Blueprint"
   - Connect your GitHub repo
   - Render will read `render.yaml` automatically
   - Click "Apply"

This will create everything correctly from the yaml file.

---

## Summary

**Quick Fix**: 
- Settings → Start Command → Change to `gunicorn dist.wsgi:application`
- Settings → Root Directory → Set to `dist`
- Manual Deploy

**That's all you need to do!** 🚀
