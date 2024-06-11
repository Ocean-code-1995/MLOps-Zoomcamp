import requests
from io import BytesIO
import pandas as pd


if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs):
    response = requests.get("https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet")

    if response.status_code != 200:
                raise Exception(response.text)
    cols = cols_to_read = ['tpep_dropoff_datetime', 'tpep_pickup_datetime', 'PULocationID', 'DOLocationID']
    df = pd.read_parquet(BytesIO(response.content), columns=cols)
    print(f"Shape: {df.shape}")
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'