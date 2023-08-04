import psycopg2
from sqlalchemy import create_engine

def load(fact_table, passenger_count_dim, trip_distance_dim, rate_code_dim, payment_type_dim, datetime_dim, pickup_location_dim, dropoff_location_dim):
    # Replace the connection parameters with your PostgreSQL database information
    connection_params = {
        "host": "localhost",
        "database": "uber1",
        "user": "postgres",
        "password": "postgres",
        "port": "5432",
    }

    # Create a PostgreSQL connection using psycopg2
    connection = psycopg2.connect(**connection_params)

    # Create an SQLAlchemy engine from the connection
    engine = create_engine('postgresql+psycopg2://', creator=lambda: connection)

    # Save each DataFrame to PostgreSQL using the engine
    datetime_dim.to_sql("datetime_dim", engine, if_exists="replace", index=False)
    passenger_count_dim.to_sql("passenger_count_dim", engine, if_exists="replace", index=False)
    trip_distance_dim.to_sql("trip_distance_dim", engine, if_exists="replace", index=False)
    rate_code_dim.to_sql("rate_code_dim", engine, if_exists="replace", index=False)
    pickup_location_dim.to_sql("pickup_location_dim", engine, if_exists="replace", index=False)
    dropoff_location_dim.to_sql("dropoff_location_dim", engine, if_exists="replace", index=False)
    payment_type_dim.to_sql("payment_type_dim", engine, if_exists="replace", index=False)
    fact_table.to_sql("fact_table", engine, if_exists="replace", index=False)

    # Close the connection
    connection.close()
    print("Data has been loaded successfully")