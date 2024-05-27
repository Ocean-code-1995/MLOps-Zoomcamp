# store all artifacts in sqlite:
mlflow ui --backend-store-uri sqlite:///mlflow.db

# search for specific models in mlflow search bar:
tags.model = 'xgboost'

# search for models based on filter:
metrics.rmse < 0.7