# Online Bookstore

A multi-container application built using:

- **Flask** (Backend)
- **React** (Frontend)
- **PostgreSQL** (Database)
- **Redis + Celery** (Task Queue)
- **Docker Compose** for container orchestration

## 🚀 Run Locally

```bash
docker-compose up --build

This project demonstrates a production-style multi-container setup where:

The backend serves APIs and connects to PostgreSQL

The frontend communicates with backend over Docker network

The worker handles asynchronous tasks using Celery + Redis
