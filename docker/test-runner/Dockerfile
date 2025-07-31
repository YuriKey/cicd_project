# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем зависимости для работы с Selenium
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Chrome для Selenium
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Копируем зависимости проекта
COPY requirements.txt /tmp/requirements.txt

# Устанавливаем зависимости с кэшированием
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Копируем весь проект
WORKDIR /app
COPY . .

# Команда для запуска тестов
CMD ["pytest"]