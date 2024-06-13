import os
import pickle

import mlflow
from flask import Flask, request, jsonify
from mlflow.tracking import MlflowClient
from sklearn.pipeline import make_pipeline

#MLFLOW_TRACKING_URI = "http://0.0.0.0:5000"
#mlflow.set_tracking_uri(MLFLOW_TRACKING_URI)


RUN_ID = os.getenv('RUN_ID')    #"614b73140c084d6392aa3bb08db42005"


logged_model = f'gs://mlflow-artifacts-1/2/{RUN_ID}/artifacts/model'

model = mlflow.pyfunc.load_model(logged_model)

def prepare_features(ride):
    features = {
        'PU_DO': f"{ride['PULocationID']}_{ride['DOLocationID']}",
        'trip_distance': ride['trip_distance']
    }
    return features

def predict_model(features):
    preds = model.predict(features)
    return float(preds[0])

app = Flask('duration-prediction')

@app.route('/predict', methods=['POST'])
def predict_endpoint():
    try:
        ride = request.get_json()
        features = prepare_features(ride)
        pred = predict_model(features)
        result = {
            'duration': pred,
            'model_version': RUN_ID
        }
        return jsonify(result)
    except Exception as e:
        app.logger.error(f'Error processing request: {e}')
        return jsonify({'error': str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
