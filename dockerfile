# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN pip install gekko

COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Command to run the application
CMD ["/app/run.sh"]
