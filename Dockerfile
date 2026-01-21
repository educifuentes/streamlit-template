# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.12-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir reduces image size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 8080
EXPOSE 8080

# Run streamlit when the container launches
# server.port=8080 is required by Cloud Run
# server.address=0.0.0.0 is required for external access
CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.address=0.0.0.0"]
