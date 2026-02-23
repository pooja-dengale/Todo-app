# Production Deployment Checklist

Use this checklist before deploying to production.

## Security

- [ ] `DEBUG = False` in production
- [ ] `SECRET_KEY` is unique and kept secret (not in version control)
- [ ] `ALLOWED_HOSTS` is properly configured
- [ ] HTTPS is enforced (`SECURE_SSL_REDIRECT = True`)
- [ ] Secure cookies enabled (`SESSION_COOKIE_SECURE = True`)
- [ ] CSRF protection configured (`CSRF_COOKIE_SECURE = True`)
- [ ] HSTS headers enabled
- [ ] X-Frame-Options set to DENY
- [ ] Content Security Policy configured
- [ ] SQL injection protection (using Django ORM)
- [ ] XSS protection enabled

## Database

- [ ] Using PostgreSQL (not SQLite) in production
- [ ] Database credentials are secure
- [ ] Database backups configured
- [ ] Migrations are up to date
- [ ] Database connection pooling enabled
- [ ] Database SSL connection enabled

## Static Files

- [ ] `collectstatic` runs successfully
- [ ] WhiteNoise is configured
- [ ] Static files are compressed
- [ ] STATIC_ROOT is set correctly
- [ ] CSS and JS files load properly

## Performance

- [ ] Gunicorn workers configured (4+ workers)
- [ ] Database queries optimized
- [ ] Pagination implemented for large datasets
- [ ] Static files cached properly
- [ ] Connection pooling enabled

## Monitoring & Logging

- [ ] Application logs are accessible
- [ ] Error tracking configured
- [ ] Health check endpoint working (`/health/`)
- [ ] Performance monitoring enabled
- [ ] Uptime monitoring configured

## Testing

- [ ] All tests pass (`python manage.py test`)
- [ ] Manual testing completed
- [ ] User registration works
- [ ] Login/logout works
- [ ] CRUD operations work
- [ ] Search and filter work
- [ ] Pagination works

## Environment Variables

- [ ] All required environment variables set:
  - [ ] SECRET_KEY
  - [ ] DEBUG
  - [ ] DATABASE_URL
  - [ ] ALLOWED_HOSTS
  - [ ] RENDER_EXTERNAL_HOSTNAME (for Render)
  - [ ] CSRF_TRUSTED_ORIGINS

## Deployment

- [ ] Code pushed to GitHub
- [ ] Build script (`build.sh`) is executable
- [ ] `requirements.txt` is up to date
- [ ] `runtime.txt` specifies Python version
- [ ] `render.yaml` configured (for Render)
- [ ] Procfile configured (for Heroku)

## Post-Deployment

- [ ] Superuser account created
- [ ] Admin panel accessible
- [ ] Test user registration
- [ ] Test task creation
- [ ] Test all CRUD operations
- [ ] Verify email functionality (if configured)
- [ ] Check error pages (404, 500)
- [ ] Verify HTTPS redirect works
- [ ] Test on mobile devices

## Documentation

- [ ] README.md updated
- [ ] Deployment guide available
- [ ] API documentation (if applicable)
- [ ] User guide available

## Backup & Recovery

- [ ] Database backup strategy in place
- [ ] Backup restoration tested
- [ ] Disaster recovery plan documented

## Compliance

- [ ] Privacy policy available (if collecting user data)
- [ ] Terms of service available
- [ ] GDPR compliance (if applicable)
- [ ] Cookie consent (if applicable)

## Optional Enhancements

- [ ] Custom domain configured
- [ ] Email service configured (SendGrid, Mailgun)
- [ ] Redis caching configured
- [ ] CDN for static files
- [ ] Rate limiting implemented
- [ ] API rate limiting
- [ ] Automated backups
- [ ] CI/CD pipeline

---

## Quick Commands

### Test locally with production settings
```bash
export DEBUG=False
export DATABASE_URL=postgresql://...
python manage.py check --deploy
```

### Run security checks
```bash
python manage.py check --deploy
```

### Collect static files
```bash
python manage.py collectstatic --noinput
```

### Run migrations
```bash
python manage.py migrate
```

### Create superuser
```bash
python manage.py createsuperuser
```

### Test the application
```bash
python manage.py test
```

---

**Last Updated:** Check this list before every production deployment!
