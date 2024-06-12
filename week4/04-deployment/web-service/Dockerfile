FROM python:3.9.7-slim

RUN pip install -U pip
RUN pip install pipenv

# Create a directory for the application for any subsequent commands to be run in this directory U(RUN, CMD, ENTRYPOINT, COPY, and ADD commands)
WORKDIR /app

# Copy the Pipfile and Pipfile.lock into the container
COPY [ "Pipfile", "Pipfile.lock", "./" ]

# Install dependencies directly into the system without creating a virtual environment
RUN pipenv install --system --deploy

# Copy the application code into the container
COPY [ "predict.py", "lin_reg.bin", "./" ]

# Expose the port that the app runs on (meaning that the container will listen on this port) -> it needs to be exposed for networking to work
EXPOSE 9696

# Define the command that will run when the container starts
ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "predict:app" ]