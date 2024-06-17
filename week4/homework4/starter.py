import argparse
import pickle
import pandas as pd

def parse_args():
    parser = argparse.ArgumentParser(description="Process the year and month for the dataset.")
    parser.add_argument('--year', type=str, required=True, help='Year of the dataset')
    parser.add_argument('--month', type=str, required=True, help='Month of the dataset')
    return parser.parse_args()

def read_data(filename):
    df = pd.read_parquet(filename)
    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60
    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()
    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    return df

args = parse_args()
YEAR = args.year
MONTH = args.month

with open('model.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

df = read_data(f'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{YEAR}-{MONTH}.parquet')
df.head()

categorical = ['PULocationID', 'DOLocationID']
dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = model.predict(X_val)


# Answer for Q5
print("Mean of yhat: ", y_pred.mean())
