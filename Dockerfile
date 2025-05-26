
# backend/Dockerfile

# Use official Python image
FROM python:3.10

# Set working directory inside container
WORKDIR /app

# Copy dependency file and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app code
COPY . .

# Expose the Flask default port
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
=======
FROM python:3.10

WORKDIR /app

COPY backend/ /app/
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]
>>>>>>> 415a570 (Initial commit)
