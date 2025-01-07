# Use the official Python image from DockerHub
FROM python:3.13.1-alpine3.21

# Set the working directory in the container
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY src/ ./src

# Specify the command to run the script
CMD ["python", "src/main.py"]
