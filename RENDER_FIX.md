# Fix Render Deployment Error

## The Problem

You got this error:
```
ModuleNotFoundError: No module named 'app'
```

This happens because Render is looking in the wrong directory.

## Solution: Update Your Repository

### Option 1: Push Only the `dist` Folder (Recommended)

If you want to deploy only the Django app:

```bash
# Go into the dist folder
cd dist

# Initialize git here (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Django todo app for Render"

# Add remote (replace YOUR_USERNAME and YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Force push (this replaces everything)
git push -f origin main
```

Now Render will see the correct structure!

### Option 2: Keep Current Structure and Update render.yaml

If you already pushed the parent directory:

1. The `render.yaml` has been updated with `rootDir: dist`
2. Push the updated file:

```bash
# From the parent directory (where you see the dist folder)
cd dist
git add render.yaml
git commit -m "Fix Render root directory"
git push origin main
```

3. In Render Dashboard:
   - Go to your web service
   - Click "Manual Deploy" → "Deploy latest commit"

## Verify Your GitHub Repository

Check what's in your GitHub repository:

1. Go to https://github.com/YOUR_USERNAME/YOUR_REPO
2. Look at the files

**Should see ONE of these structures:**

### Structure A (Recommended):
```
your-repo/
├── manage.py
├── requirements.txt
├── render.yaml
├── build.sh
├── dist/
│   ├── settings.py
│   └── ...
└── todo/
    └── ...
```

### Structure B (Also works):
```
your-repo/
├── dist/
│   ├── manage.py
│   ├── requirements.txt
│   ├── render.yaml
│   ├── build.sh
│   ├── dist/
│   │   ├── settings.py
│   │   └── ...
│   └── todo/
│       └── ...
```

If you have Structure B, the updated `render.yaml` with `rootDir: dist` will fix it.

## Quick Fix Steps

1. **Update render.yaml** (already done above)

2. **Push to GitHub:**
```bash
cd dist
git add render.yaml
git commit -m "Add rootDir to render.yaml"
git push origin main
```

3. **Redeploy on Render:**
   - Render will auto-deploy when you push
   - OR manually: Dashboard → Your Service → "Manual Deploy"

4. **Check logs:**
   - Dashboard → Your Service → "Logs"
   - Should see: "Build successful 🎉"

## Alternative: Manual Configuration in Render

If the yaml doesn't work, configure manually:

1. **Render Dashboard** → Your Web Service → **Settings**

2. **Root Directory**: Set to `dist` (if your repo has the parent structure)

3. **Build Command**: `./build.sh`

4. **Start Command**: `gunicorn dist.wsgi:application`

5. Click **"Save Changes"**

6. Click **"Manual Deploy"** → **"Deploy latest commit"**

## Test After Fix

Once deployed successfully:

1. **Health Check**: `https://your-app.onrender.com/health/`
   - Should return: `{"status": "healthy"}`

2. **Main App**: `https://your-app.onrender.com`
   - Should show login page

3. **Create Superuser**:
   - Dashboard → Shell
   - Run: `python manage.py createsuperuser`

## Still Having Issues?

### Check Build Logs

Look for these in Render logs:

✅ **Good signs:**
```
==> Installing dependencies...
Successfully installed Django-5.0.1 ...
127 static files copied
==> Build successful 🎉
```

❌ **Bad signs:**
```
ModuleNotFoundError: No module named 'app'
ModuleNotFoundError: No module named 'dist'
```

### Common Issues

**Issue**: `No module named 'dist'`
**Fix**: Your Django project folder is named `dist`. This is correct. Make sure `startCommand` is `gunicorn dist.wsgi:application`

**Issue**: `Permission denied: ./build.sh`
**Fix**: 
```bash
git update-index --chmod=+x build.sh
git commit -m "Make build.sh executable"
git push
```

**Issue**: Build succeeds but app won't start
**Fix**: Check the Start Command is exactly: `gunicorn dist.wsgi:application`

## Need More Help?

1. **Check your GitHub repo structure** - Make sure files are in the right place
2. **Check Render logs** - Look for specific error messages
3. **Verify render.yaml** - Should have `rootDir: dist` if needed
4. **Try manual configuration** - Use Render Dashboard settings

---

## Summary

The fix is simple:

1. ✅ Updated `render.yaml` with `rootDir: dist`
2. ✅ Push to GitHub
3. ✅ Render auto-redeploys
4. ✅ App should work!

If you pushed only the `dist` folder contents to GitHub (recommended), you don't need `rootDir` at all.
