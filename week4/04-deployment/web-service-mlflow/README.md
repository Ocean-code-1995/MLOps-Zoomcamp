## Getting the model for deployment from MLflow

* Take the code from the previous video
* Train another model, register with MLflow
* Put the model into a scikit-learn pipeline
* Model deployment with tracking server
* Model deployment without the tracking server

Starting the MLflow server with S3:

```bash
mlflow server \
    --backend-store-uri=sqlite:///mlflow.db \
    --default-artifact-root=s3://mlflow-models-alexey/
```

Downloading the artifact

```bash
export MLFLOW_TRACKING_URI="http://127.0.0.1:5000"
export MODEL_RUN_ID="6dd459b11b4e48dc862f4e1019d166f6"

mlflow artifacts download \
    --run-id ${MODEL_RUN_ID} \
    --artifact-path model \
    --dst-path .
```

-----------------

# MLOps Zoomcamp 4.3 - Web-services: Getting the models from the model registry (MLflow)
---
## Dependent on tracking server

1) Put registered model to flask application

Starting MLflow server with gcp:

 ```bash
 - mlflow server \
  --backend-store-uri postgresql://mlflow_user_new:___XXX___@localhost/mlflow \
  --default-artifact-root gs://mlflow-artifacts-1 \
  --host 0.0.0.0 --port 5000

  pipenv environment:
  ```bash
  pip install pipenv
  pipenv install mlflow     # creates new env also
  pipenv shell              # activate
  ```

install google dependencies:
  ```bash
  pipenv install google.cloud google.auth google-cloud-storage
  ```
run random_forest.ipynb to have a registered pipeline!

run:
  ```bash
  python predict.py
  python test.py
  ```

  

## How to become independent from tracking server
in predict.py set "   RUN_ID = os.getenv('RUN_ID')   "

```bash
export RUN_ID="614b73140c084d6392aa3bb08db42005"
```