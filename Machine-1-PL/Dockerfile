# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

VOLUME ["/mnt/data"]

# Ensure the input file exists
RUN mkdir -p /mnt/data && touch /mnt/data/input.txt

# Run file_processor.py when the container launches
CMD ["python", "file_processor.py"]
