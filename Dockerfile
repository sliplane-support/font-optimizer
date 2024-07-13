# Use an official Python runtime as a parent image
FROM python:3.12.4-slim

# COPY requirements.txt into the container
COPY requirements.txt .

# Install any needed packages
RUN pip install -r requirements.txt

# Copy app.py into the container
COPY app.py .

# Run the application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]