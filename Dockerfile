# Use Python runtime slim
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the dependency list first (helps with Docker build caching)
COPY requirements.txt .

# Install the Python libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy actual Python script into the container
COPY . .

#Set Entrypoint of script
ENTRYPOINT ["python", "pypasswd.py"]

# Run script when the container starts
CMD ["--length","10", "--bulk","50", "--verbose","False"]