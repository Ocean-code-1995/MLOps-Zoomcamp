import requests

#### The script uses the requests library to send a POST request to the Flask web service's /predict endpoint with the ride data as JSON.

# The Flask application in this setup serves as a web service to expose the machine learning model as an API. The test script sends a POST request to the /predict endpoint of the Flask app with the ride data as JSON. The Flask app processes the data, makes a prediction using the model, and sends back the prediction as JSON. The test script then prints the prediction.

# The data to send to the web service (features of the ride)
ride = {
    "PULocationID":  10,
    "DOLocationID":  50,
    "trip_distance": 40
}

# The URL of the web service
url = 'http://localhost:9696/predict'

# Send the request to the web service
response = requests.post(url, json=ride)

# Print the response
print(response.json())


# Execution in Terminal
# ----------------------------------------------------------------------------------
# When you run python test.py in the terminal, it executes the test script, which sends data to the Flask app running locally. Assuming the Flask app (predict.py) is running and listening on localhost at port 9696, it will receive the POST request, process the data, and send back the prediction, which is then printed by the test script. Make sure that predict.py is running before you execute test.py to ensure the test script can communicate with the Flask web service.