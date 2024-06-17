# Deploying a model as a web-service
---

* Creating a virtual environment with Pipenv
* Creating a script for predictiong 
* Putting the script into a Flask app
* Packaging the app to Docker


# MLOps Zoomcamp 4.2 - Web-services: Deploying models with Flask and Docker
---

## Overview
Flask is utilized to create a web service that exposes a machine learning model via an API. This setup enables external applications to interact with the model, sending data to be processed and receiving predictions.

## Key Components

### Flask Application
- **Role**: Serves as the API endpoint where the machine learning model is hosted.
- **Functionality**:
  - Receives data through API calls.
  - Processes the data by making predictions.
  - Returns the predictions in response to the requests.
- **Environment**: Runs on the local machine, accessible via `localhost`.

### Localhost
- **Definition**: Refers to the local computer where the server (Flask app) is running.
- **Access**: Accessed through the URL `http://localhost:[port]`, where `[port]` is the port number on which the Flask server is listening.
- **Usage**: Commonly used for development and testing within a secure and private environment before deploying the application to a public server.

## Workflow

1. **Flask Server Setup**
   - A Flask instance is created and configured to listen on a specific port on the local machine.
   - An endpoint (e.g., `/predict`) is defined to accept POST requests containing input data for predictions.

2. **Client Interaction**
   - A client script (e.g., `test.py`) sends a POST request to the Flask server with necessary data.
   - Flask processes the request, applies the model to the input data, and sends back the prediction as a JSON response.

3. **Running the Flask App**
   - Typically executed by a command like `python app.py`, which starts the Flask server.
   - Accessible locally at `http://localhost:9696` if configured to run on port 9696.

## Example Use Case

- **Machine Learning Model**: Predicts the duration of a ride based on input features like pickup and dropoff locations, and trip distance.
- **Client Request**:
  ```python
  import requests
  url = 'http://localhost:9696/predict'
  ride = {"PULocationID": 10, "DOLocationID": 50, "trip_distance": 40}
  response = requests.post(url, json=ride)
  print(response.json())

## **Get rid of error [WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.]***
- use production server `"gunicorn"` instead of "flask"

```bash
gunicorn --bind=0.0.0.0:9696 predict:app
python test.py
```
-> go to predict module and look for variable with name "app"

- `flask is solely used for local development purposes!!


### Genral workflow steps:

1) Development Testing:
- 1st terminal:

```bash
python predict.py
```
- In another terminal:
```bash
python test.py
```
2) Production like testing with unicorn:

```bash
gunicorn --bind=0.0.0.0:9696 predict:app
python test.py
```



## Docker Application

- build docker image (-t: 'tag'):
    - name:tag. Tags are useful for versioning images.
```bash
docker build -t ride-duration-prediction-service:v1 .
```

- creates a writable container layer over the specified image and starts it using the specified command:
```bash
docker run -it --rm -p 9696:9696  ride-duration-prediction-service:v1
```
