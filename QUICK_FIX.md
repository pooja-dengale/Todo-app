# 🚨 Quick Fix for "No module named 'app'" Error

## The Problem

Render is looking for your Django app in the wrong place.

## The Solution (Choose One)

### ✅ Solution 1: Push Only the `dist` Folder (EASIEST)

This is the cleanest approach:

```bash
# 1. Go into the dist folder
cd dist

# 2. Remove old git if it exists
rm -rf .git

# 3. Start fresh
git init
git add .
git commit -m "Django todo app for Render"

# 4. Push to GitHub (replace YOUR_USERNAME and YOUR_REPO)
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -f origin main
```

**What this does**: Makes your GitHub repo look like this:
```
your-repo/
├── manage.py          ← At root level
├── requirements.txt
├── render.yaml
├── build.sh
├── dist/             ← Django project folder
│   ├── settings.py
│   └── wsgi.py
└── todo/             ← Django app folder
```

Then in Render:
- It will auto-deploy correctly
- No configuration needed!

---

### ✅ Solution 2: Update Render Settings (If you already pushed)

If you already pushed and don't want to redo it:

```bash
# 1. Make sure render.yaml has rootDir
cd dist
git add render.yaml
git commit -m "Add rootDir to render.yaml"
git push origin main
```

**2. Update Render Dashboard:**
- Go to https://dashboard.render.com
- Click your web service
- Click "Settings" (left sidebar)
- Find "Root Directory"
- Set it to: `dist`
- Click "Save Changes"
- Click "Manual Deploy" → "Deploy latest commit"

---

## How to Know Which Solution to Use?

### Check Your GitHub Repository

Go to your GitHub repo: `https://github.com/YOUR_USERNAME/YOUR_REPO`

**If you see this** (manage.py at root):
```
✅ CORRECT - No fix needed
your-repo/
├── manage.py
├── requirements.txt
├── render.yaml
```

**If you see this** (dist folder at root):
```
❌ NEEDS FIX
your-repo/
└── dist/
    ├── manage.py
    ├── requirements.txt
```

Use Solution 1 or Solution 2 above.

---

## After Applying the Fix

1. **Wait for Render to rebuild** (5-10 minutes)

2. **Check the logs** in Render Dashboard:
   - Should see: `==> Build successful 🎉`
   - Should see: `Booting worker with pid: ...`

3. **Test your app**:
   - Visit: `https://your-app-name.onrender.com/health/`
   - Should return: `{"status": "healthy"}`

4. **Create superuser**:
   - Render Dashboard → Shell
   - Run: `python manage.py createsuperuser`

5. **Access your app**:
   - Visit: `https://your-app-name.onrender.com`

---

## Still Not Working?

### Double-check these:

1. **GitHub repo structure**: `manage.py` should be at root level
2. **render.yaml location**: Should be at root level (next to manage.py)
3. **Start command**: Should be `gunicorn dist.wsgi:application`
4. **Build command**: Should be `./build.sh`

### View detailed logs:

1. Render Dashboard → Your Service
2. Click "Logs"
3. Look for error messages
4. Share the error if you need help

---

## Need More Help?

See the detailed guide: [RENDER_FIX.md](RENDER_FIX.md)

---

**TL;DR**: Go into the `dist` folder, push from there. Your GitHub repo should show `manage.py` at the root level, not inside a `dist` folder.
