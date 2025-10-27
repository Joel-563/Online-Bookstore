from app import celery

# The tasks are already defined in app.py (process_order)
# Run worker with: celery -A app.celery worker --loglevel=info
