# Use an official Python runtime as a parent image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
# libgl1-mesa-glx and libglib2.0-0 are for opencv
# poppler-utils and tesseract-ocr are for unstructured
# libmagic-dev is for filetype detection
# build-essential is for building python packages that might need compilation
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1 \
    libglib2.0-0 \
    poppler-utils \
    tesseract-ocr \
    libmagic-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the application using fastapi dev
# The --host 0.0.0.0 is crucial for docker containers to be accessible from outside
CMD ["fastapi", "dev", "app.py", "--host", "0.0.0.0", "--port", "8000"]
