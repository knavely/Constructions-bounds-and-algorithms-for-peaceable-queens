# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY even_torus.py /app/even_torus.py
COPY odd_torus.py /app/odd_torus.py
COPY regular_board.py /app/regular_board.py

RUN pip install gekko

COPY run.sh /app/run.sh
RUN chmod +x /app/run.sh

# Command to run the application
CMD ["/app/run.sh"]
