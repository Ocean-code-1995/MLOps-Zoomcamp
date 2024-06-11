if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def train_vectorize(df, *args, **kwargs):
    X, y = df[['PULocationID', 'DOLocationID']], df['duration']
    encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=True)
    X_encoded = encoder.fit_transform(X)
    model = LinearRegression().fit(X_encoded, y)
    
    print(f"Training completed. Y-intercept: {model.intercept_}")
    return {'encoder': encoder, 'model': model}  # Return as a dictionary


@test
def test_model_and_encoder(output):
    encoder, model = output
    assert encoder is not None, "Encoder is undefined"
    assert model is not None, "Model is undefined"
    assert hasattr(model, 'intercept_'), "Model is not properly trained"