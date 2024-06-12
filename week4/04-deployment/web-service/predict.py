import pickle

from flask import Flask, request, jsonify

# load the model and the dict vectorizer
with open('lin_reg.bin', 'rb') as f_in:
    (dv, model) = pickle.load(f_in)


def prepare_features(ride):
    features = {}
    features['PU_DO'] = '%s_%s' % (ride['PULocationID'], ride['DOLocationID'])
    features['trip_distance'] = ride['trip_distance']
    return features


def predict(features):
    X = dv.transform(features)
    preds = model.predict(X)
    return float(preds[0])


# Wrapper for the Flask web service
app = Flask('duration-prediction')

# The endpoint to predict the duration of a ride
@app.route('/predict', methods=['POST'])
def predict_endpoint():
    ride     = request.get_json()     # Get the ride data from the request
    features = prepare_features(ride) # Prepare the features
    pred     = predict(features)      # Predict the duration of the ride

    result = {
        'duration': pred
    }

    return jsonify(result)           # Return the result as JSON


if __name__ == "__main__":
    # Run the Flask web service
    app.run(debug=True, host='0.0.0.0', port=9696)