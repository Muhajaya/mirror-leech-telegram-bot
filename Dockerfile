FROM anasty17/mltb:latest

# Set working directory
WORKDIR /usr/src/app

# Install essential tools
RUN apt-get update && apt-get install -y \
  rclone \
  aria2 \
  ffmpeg \
  p7zip-full \
  curl \
  unzip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# (Optional) make dir writable
RUN chmod -R 777 /usr/src/app

# Python environment setup
RUN python3 -m venv mltbenv

# Copy Python dependencies and install
COPY requirements.txt .
RUN mltbenv/bin/pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

# Start script
CMD ["bash", "start.sh"]
