from components.extract import extract
from components.transform import transform
from components.load import load

if __name__ == "__main__":
    data=extract('uber_data.csv')
    fact_table, passenger_count_dim, trip_distance_dim, rate_code_dim, payment_type_dim, datetime_dim, pickup_location_dim, dropoff_location_dim = transform(data)
    load(fact_table, passenger_count_dim, trip_distance_dim, rate_code_dim, payment_type_dim, datetime_dim, pickup_location_dim, dropoff_location_dim)