FROM python:3.11-slim

# Установка зависимостей с очисткой кэша в одном RUN
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    gnupg \  # Добавляем необходимый пакет
    && wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | gpg --dearmor -o /usr/share/keyrings/googlechrome-linux-keyring.gpg \
    && echo "deb [arch=amd64 signed-by=/usr/share/keyrings/googlechrome-linux-keyring.gpg] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && rm -rf /var/lib/apt/lists/*

# Копирование зависимостей
COPY requirements.txt /tmp/requirements.txt

# Установка Python-зависимостей с кэшированием
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Копирование всего проекта
WORKDIR /app
COPY . .

# Команда для запуска тестов
CMD ["pytest"]