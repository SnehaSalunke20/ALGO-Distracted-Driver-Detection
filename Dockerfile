# Use an official lightweight Python image as the base
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker's layer caching
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application's code into the container
COPY . .

# Expose the port that Streamlit runs on (default is 8501)
EXPOSE 8501

# The command to run your Streamlit application when the container starts
CMD ["streamlit", "run", "app.py"]

