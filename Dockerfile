FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy Django project only (topics mounted as volumes)
COPY acsl_portal/ ./acsl_portal/

# Set working directory to Django project
WORKDIR /app/acsl_portal

# Expose port
EXPOSE 8000

# Run Django dev server (simpler for development)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
