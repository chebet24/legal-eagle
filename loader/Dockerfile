# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
# --no-cache-dir: Disables the cache to keep the image size smaller
# -r: Install from the given requirements file.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the local code to the container
COPY main.py .

# Set the command to run the function
# functions-framework will automatically use the PORT environment variable
# provided by Cloud Run.
CMD ["functions-framework", "--target=process_file", "--port=8080"]
