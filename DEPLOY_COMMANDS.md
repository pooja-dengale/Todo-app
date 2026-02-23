# Deploy Commands - Copy & Paste

## 🚀 Deploy to Render (Correct Way)

### Step 1: Navigate to dist folder
```bash
cd dist
```

### Step 2: Initialize Git (if needed)
```bash
git init
```

### Step 3: Add all files
```bash
git add .
```

### Step 4: Commit
```bash
git commit -m "Production-ready Django todo app"
```

### Step 5: Add GitHub remote
**Replace YOUR_USERNAME and YOUR_REPO with your actual GitHub username and repository name**

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

### Step 6: Push to GitHub
```bash
git branch -M main
git push -u origin main
```

If you get an error about existing remote:
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

---

## 🔧 Fix "No module named 'app'" Error

### Option A: Start Fresh (Recommended)
```bash
cd dist
rm -rf .git
git init
git add .
git commit -m "Django todo app"
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -f origin main
```

### Option B: Update render.yaml
```bash
cd dist
git add render.yaml
git commit -m "Fix root directory"
git push origin main
```

Then in Render Dashboard:
- Settings → Root Directory → Set to `dist`
- Save Changes → Manual Deploy

---

## 📝 After Deployment

### Create Superuser (in Render Shell)
```bash
python manage.py createsuperuser
```

### Test Health Check
```bash
curl https://your-app-name.onrender.com/health/
```

### View Logs
```bash
# In Render Dashboard → Logs tab
```

---

## 🔄 Update Your App

### Make changes and redeploy
```bash
cd dist
git add .
git commit -m "Your update message"
git push origin main
```

Render will automatically redeploy!

---

## 🛠️ Useful Git Commands

### Check current status
```bash
git status
```

### View commit history
```bash
git log --oneline
```

### Check remote URL
```bash
git remote -v
```

### Change remote URL
```bash
git remote set-url origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

### Force push (use carefully!)
```bash
git push -f origin main
```

---

## 📍 Important Paths

### Your GitHub repo should look like:
```
your-repo/
├── manage.py          ← Should be at root
├── requirements.txt
├── render.yaml
├── build.sh
├── dist/             ← Django project
└── todo/             ← Django app
```

### NOT like this:
```
your-repo/
└── dist/             ← Wrong! Too nested
    ├── manage.py
    └── ...
```

---

## ✅ Verification Checklist

After pushing to GitHub, verify:

- [ ] Go to your GitHub repo in browser
- [ ] See `manage.py` at root level (not inside dist folder)
- [ ] See `render.yaml` at root level
- [ ] See `requirements.txt` at root level
- [ ] See `build.sh` at root level

If all checked, you're good to deploy on Render!

---

## 🆘 Quick Troubleshooting

### Error: "Permission denied"
```bash
git update-index --chmod=+x build.sh
git commit -m "Make build.sh executable"
git push
```

### Error: "fatal: remote origin already exists"
```bash
git remote remove origin
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

### Error: "Updates were rejected"
```bash
git pull origin main --rebase
git push origin main
```

Or force push (overwrites remote):
```bash
git push -f origin main
```

---

## 📞 Need Help?

1. Check [QUICK_FIX.md](QUICK_FIX.md) for common errors
2. Check [RENDER_QUICK_START.md](RENDER_QUICK_START.md) for full guide
3. View Render logs in Dashboard
4. Check GitHub repo structure

---

**Pro Tip**: Always run commands from inside the `dist` folder!
