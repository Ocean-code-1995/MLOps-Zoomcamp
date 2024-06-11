import mlflow
from mlflow import sklearn as mlflow_sklearn
import joblib

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_model_and_vectorizer(*args, **kwargs):
    # Handling kwargs directly or unpacking args if kwargs are not provided
    if kwargs:
        encoder = kwargs.get('encoder')
        model = kwargs.get('model')
    elif args and len(args) == 1 and isinstance(args[0], dict):
        # Assuming the dictionary is passed as a single positional argument
        data_dict = args[0]
        encoder = data_dict.get('encoder')
        model = data_dict.get('model')
    else:
        raise ValueError("Function expects keyword arguments for 'encoder' and 'model'")

    # Ensure MLFlow is tracking
    mlflow.set_tracking_uri('http://mlflow:5000')
    
    # Start MLFlow experiment
    import mlflow
from mlflow import sklearn as mlflow_sklearn
import joblib

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter


@data_exporter
def export_model_and_vectorizer(*args, **kwargs):
    # Handling kwargs directly or unpacking args if kwargs are not provided
    if kwargs:
        encoder = kwargs.get('encoder')
        model = kwargs.get('model')
    elif args and len(args) == 1 and isinstance(args[0], dict):
        # Assuming the dictionary is passed as a single positional argument
        data_dict = args[0]
        encoder = data_dict.get('encoder')
        model = data_dict.get('model')
    else:
        raise ValueError("Function expects keyword arguments for 'encoder' and 'model'")

    # Ensure MLFlow is tracking
    mlflow.set_tracking_uri('http://mlflow:5000')
    
    # Start MLFlow experiment
    with mlflow.start_run():
        # Log the linear regression model
        mlflow_sklearn.log_model(model, "linear_regression_model")
        
        # Log the OneHotEncoder as an artifact
        # We need to save it to a file first
        with open("vectorizer.pkl", "wb") as f:
            joblib.dump(encoder, f)
        mlflow.log_artifact("vectorizer.pkl", artifact_path="artifacts")
        
        # Optionally, you can log other metrics or parameters
        mlflow.log_param("model_type", "linear_regression")

        # Finish the MLFlow run
        run_id = mlflow.active_run().info.run_id
    return f"Model and vectorizer logged with Run ID: {run_id}"



