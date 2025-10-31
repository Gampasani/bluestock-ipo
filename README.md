# Bluestock IPO Web Application (Django + DRF)

## Quickstart (Local)
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# Dev DB uses SQLite by default. For Postgres, set DATABASE_URL env var.
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

- Home: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin
- API list: http://127.0.0.1:8000/api/ipo/
- API detail: http://127.0.0.1:8000/api/ipo/1/

## Deploy to Render
- Add env vars: `SECRET_KEY`, `DEBUG=False`, `ALLOWED_HOSTS=<your-service>.onrender.com`, `DATABASE_URL`
- Build command: `pip install -r requirements.txt && ./build.sh`
- Start command: `gunicorn bluestock_ipo.wsgi:application`
- Add a Persistent Disk and mount at `/opt/render/project/src/media` for uploads.
