# Use the official Python image as the base image
FROM python:3.8

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script to the working directory
COPY app.py .

# Install Flask and requests
RUN pip install Flask requests

# Expose the port that the app will run on
EXPOSE 5000

# Start the application
CMD ["python", "app.py"]
