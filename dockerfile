FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Install system dependencies for Playwright and optional document/OCR tools
RUN apt-get update && \
    apt-get install -y \
    wget \
    curl \
    unzip \
    libx11-dev \
    libx264-dev \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    libxss1 \
    libappindicator3-1 \
    libasound2 \
    chromium \
    antiword \
    tesseract-ocr \
    libtesseract-dev \
    libreoffice \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY ./requirements.txt /requirements.txt
RUN python -m pip install --upgrade pip && \
    pip install --no-cache-dir -r /requirements.txt

# Install Playwright and its browsers
RUN python -m playwright install

# Copy application code
COPY . /app/

# Set environment variables for headless Chromium
ENV DISPLAY=:99
ENV CHROME_BIN=/usr/bin/chromium

# Expose FastAPI application port
EXPOSE 5500

# Run FastAPI app via Uvicorn on port 5500
CMD ["uvicorn", "web_app.main:app", "--host", "0.0.0.0", "--port", "5500"]
