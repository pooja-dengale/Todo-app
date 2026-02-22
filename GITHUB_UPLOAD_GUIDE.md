# GitHub Upload Guide

## Step-by-Step Instructions to Upload Your Django ToDo App to GitHub

### Prerequisites
- Git installed on your computer
- GitHub account (create one at https://github.com if you don't have one)

---

## Method 1: Using Git Command Line (Recommended)

### Step 1: Create a GitHub Repository

1. Go to https://github.com
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Fill in the details:
   - **Repository name:** `django-todo-app` (or your preferred name)
   - **Description:** "A full-featured ToDo application built with Django 5"
   - **Visibility:** Choose Public or Private
   - **DO NOT** check "Initialize this repository with a README" (we already have one)
5. Click "Create repository"

### Step 2: Initialize Git in Your Project

Open your terminal/command prompt and navigate to the dist folder:

```bash
cd dist
```

Initialize Git repository:

```bash
git init
```

### Step 3: Add Files to Git

Add all files to staging:

```bash
git add .
```

Check what will be committed:

```bash
git status
```

### Step 4: Create First Commit

```bash
git commit -m "Initial commit: Django ToDo application with authentication"
```

### Step 5: Connect to GitHub

Replace `yourusername` and `django-todo-app` with your GitHub username and repository name:

```bash
git remote add origin https://github.com/yourusername/django-todo-app.git
```

### Step 6: Push to GitHub

For the first push:

```bash
git branch -M main
git push -u origin main
```

### Step 7: Verify Upload

1. Go to your GitHub repository URL
2. Refresh the page
3. You should see all your files uploaded!

---

## Method 2: Using GitHub Desktop (Easier for Beginners)

### Step 1: Download GitHub Desktop

1. Go to https://desktop.github.com/
2. Download and install GitHub Desktop
3. Sign in with your GitHub account

### Step 2: Add Your Project

1. Click "File" → "Add Local Repository"
2. Browse to your `dist` folder
3. Click "Add Repository"
4. If prompted to create a repository, click "Create Repository"

### Step 3: Make Initial Commit

1. You'll see all your files in the "Changes" tab
2. Add a commit message: "Initial commit: Django ToDo application"
3. Click "Commit to main"

### Step 4: Publish to GitHub

1. Click "Publish repository" button
2. Choose repository name: `django-todo-app`
3. Add description: "A full-featured ToDo application built with Django 5"
4. Choose Public or Private
5. Click "Publish Repository"

### Step 5: Verify

1. Click "View on GitHub" button
2. Your repository should open in your browser!

---

## Method 3: Using VS Code (If you use VS Code)

### Step 1: Open Project in VS Code

```bash
cd dist
code .
```

### Step 2: Initialize Git

1. Click the Source Control icon (left sidebar)
2. Click "Initialize Repository"

### Step 3: Stage and Commit

1. Click the "+" icon next to "Changes" to stage all files
2. Type commit message: "Initial commit: Django ToDo application"
3. Click the checkmark icon to commit

### Step 4: Publish to GitHub

1. Click "Publish to GitHub" button
2. Choose repository name and visibility
3. Click "Publish"

---

## After Upload: Update README

Don't forget to update the README.md file with:
- Your actual GitHub username
- Your name
- Add screenshots (optional but recommended)

To update:

```bash
# Edit README.md with your information
git add README.md
git commit -m "Update README with personal information"
git push
```

---

## Common Issues and Solutions

### Issue: "Permission denied (publickey)"

**Solution:** Set up SSH key or use HTTPS with personal access token

For HTTPS with token:
1. Go to GitHub Settings → Developer settings → Personal access tokens
2. Generate new token (classic)
3. Use token as password when pushing

### Issue: "Repository not found"

**Solution:** Check the remote URL

```bash
git remote -v
```

Update if needed:
```bash
git remote set-url origin https://github.com/yourusername/django-todo-app.git
```

### Issue: Files not uploading

**Solution:** Check .gitignore isn't blocking important files

```bash
git status
```

### Issue: "Failed to push some refs"

**Solution:** Pull first, then push

```bash
git pull origin main --rebase
git push origin main
```

---

## Adding Screenshots (Optional but Recommended)

1. Take screenshots of your app:
   - Login page
   - Task list
   - Task form
   - Delete confirmation

2. Create a `screenshots` folder in your repository

3. Upload screenshots:
```bash
mkdir screenshots
# Add your screenshot files to this folder
git add screenshots/
git commit -m "Add screenshots"
git push
```

4. Update README.md to include images:
```markdown
![Login Page](screenshots/login.png)
![Task List](screenshots/task-list.png)
```

---

## Next Steps After Upload

1. ✅ Add repository description on GitHub
2. ✅ Add topics/tags (django, python, todo-app, web-development)
3. ✅ Enable GitHub Pages (if you want to host documentation)
4. ✅ Add a star to your own repository
5. ✅ Share the link with others!

---

## Updating Your Repository Later

When you make changes to your code:

```bash
git add .
git commit -m "Description of changes"
git push
```

---

## Your Repository URL

After upload, your repository will be available at:
```
https://github.com/yourusername/django-todo-app
```

Share this link on your resume, portfolio, or with potential employers!

---

## Need Help?

- GitHub Docs: https://docs.github.com
- Git Basics: https://git-scm.com/book/en/v2/Getting-Started-Git-Basics
- GitHub Community: https://github.community/

Good luck! 🚀
