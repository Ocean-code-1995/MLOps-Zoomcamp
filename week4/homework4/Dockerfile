# Use the provided base image with Python and the model files
FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

# Set the working directory in the container
WORKDIR /app

# Copy your Python script into the container
COPY starter.py /app/

# Install required Python packages
# Assuming you have a requirements.txt with pandas, numpy, etc.
RUN pip install pandas numpy fastparquet pyarrow scikit-learn==1.5.0

# Command to run the script
CMD ["python", "starter.py", "--year", "2023", "--month", "05"]
