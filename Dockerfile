FROM python:3.10.6-slim-buster

RUN apt-get update && apt-get install -y \
    python3-pip \
    curl \
    unzip \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --upgrade pip

COPY . .

CMD ["tail", "-f", "/dev/null"]