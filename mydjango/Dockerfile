# Use the official Python image as a base
FROM python:3.9

# Set environment variables for Python buffering
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container at /app
COPY . /app/

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application using Gunicorn
CMD ["gunicorn", "--bind", "http://127.0.0.1:8000/", "myDjango.wsgi:application"]