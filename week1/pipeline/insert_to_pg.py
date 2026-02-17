import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

data_path = Path("data/yellow_tripdata_2021-01.csv.gz")
engine = create_engine('postgresql+psycopg://root:root@localhost:5432/ny_taxi')

dtype = {
    "VendorID": "Int64",
    "passenger_count": "Int64",
    "trip_distance": "float64",
    "RatecodeID": "Int64",
    "store_and_fwd_flag": "string",
    "PULocationID": "Int64",
    "DOLocationID": "Int64",
    "payment_type": "Int64",
    "fare_amount": "float64",
    "extra": "float64",
    "mta_tax": "float64",
    "tip_amount": "float64",
    "tolls_amount": "float64",
    "improvement_surcharge": "float64",
    "total_amount": "float64",
    "congestion_surcharge": "float64"
}

parse_dates = [
    "tpep_pickup_datetime",
    "tpep_dropoff_datetime"
]

df = pd.read_csv(
    data_path,
    nrows=1000,
    dtype=dtype,
    parse_dates=parse_dates
)

# still cant run
# print(pd.io.sql.get_schema(df, name='yellow_taxi_data', con=engine))
