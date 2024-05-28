# store all artifacts in sqlite:
mlflow ui --backend-store-uri sqlite:///mlflow.db

# search for specific models in mlflow search bar:
tags.model = 'xgboost'

# search for models based on filter:
metrics.rmse < 0.7

# Start MLFlow server (Scenario3):
mlflow server \
  --backend-store-uri postgresql://<mlflow-user>:<password>@localhost/mlflow \
  --default-artifact-root gs://<your-gcs-bucket> \
  --host 0.0.0.0 --port 5000

ALTER USER mlflow_user WITH PASSWORD 'your_new_password';
