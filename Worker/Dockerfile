FROM python:3.12-alpine
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY worker.py /app/
COPY app.py /app/
CMD ["celery","-A","app.celery","worker","--loglevel=info"]
