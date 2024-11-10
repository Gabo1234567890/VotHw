# Този файл дефинира image-a и средата на Flask web app контейнера

# Дефинира, че Docker контейнера чрез python:3.9-slim image-a
FROM python:3.9-slim

# Задава /app като работната директория за всички следващи команди в Dockerfile
WORKDIR /app

# Копира съдържанието от локалната app/ директория в /app директорията в контейнера
COPY app/ /app

# Инсталира необходимите Python dependencies в контейнера
RUN pip install -r requirements.txt

# Задава командата по подразбиране, която ще се изпълни когато контейнера бъде стартиран. В случая ще се изпълни python еxecutable-a с аргумент app.py
CMD ["python", "app.py"]
