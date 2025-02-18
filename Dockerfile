# Используем официальный образ Python
FROM python:3.11

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Выполняем миграции для Django
RUN python admin/manage.py migrate

# Открываем порты для Django (8000) и FastAPI (8001)
EXPOSE 8000 8001

# Запускаем оба сервиса (Django и FastAPI) в одном контейнере
CMD uvicorn api.main:app --host 0.0.0.0 --port 8001 & \
    python admin/manage.py runserver 0.0.0.0:8000