web: gunicorn blogger.wsgi
worker: python manage-py celery worker -A blogger.celery --loglevel=info