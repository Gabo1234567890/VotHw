# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY app/ /app

# Install Python dependencies
RUN pip install -r requirements.txt

# Command to start the app
CMD ["python", "app.py"]
