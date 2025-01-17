FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV DJANGO_SETTINGS_MODULE=booking_system.settings
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
