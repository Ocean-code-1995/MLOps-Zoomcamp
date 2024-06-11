import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LinearRegression

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@transformer
def transform(df):

    X, y = df.drop(columns="duration", axis=1), df['duration']

    #OHEncoder = OneHotEncoder(handle_unknown='ignore', sparse_output=True)
    #X_encoded = OHEncoder.fit_transform(X[['PULocationID', 'DOLocationID']])
    #model = LinearRegression().fit(X_encoded, y)
    #print(f" Y-intercept: {model.intercept_}")
    #return OHEncoder, model

    return {'features': X, 'target': y}



@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'