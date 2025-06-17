# Backend/Dockerfile

# 1. Use a known-compatible Python base image
FROM python:3.9-slim

# 2. Set working directory
WORKDIR /app

# 3. Copy and install only your pinned requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy the rest of your backend code
COPY . .

# 5. Expose the port your app uses
EXPOSE 8000

# 6. Start Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
