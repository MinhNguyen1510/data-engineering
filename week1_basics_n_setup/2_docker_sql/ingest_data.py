import argparse
import pandas as pd
from sqlalchemy import create_engine
import time
import os
import pyarrow.parquet as pq

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    database = params.db
    table_name = params.table_name
    url = params.url

    # Download file CSV
    parquet_name = "output.parquet"
    os.system(f"wget {url} -O {parquet_name}")

    parquet_file = pq.ParquetFile(parquet_name)
    batch_iter = parquet_file.iter_batches(batch_size=100000)

    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

    # df_iter = pd.read_csv('yellow_tripdata_2021-01.csv',
    #                       iterator=True,
    #                       chunksize=100000,
    #                       parse_dates=['tpep_pickup_datetime', 'tpep_dropoff_datetime'],
    #                       dtype={'store_and_fwd_flag': str})

    print("Starting iterator 1")
    try:
        start_time = time.time()
        first_batch = next(batch_iter)
        first_chunk = first_batch.to_pandas()
        first_chunk.to_sql(name=table_name,
                           con=engine,
                           if_exists='replace',
                           index=False)
        end_time = time.time()
        print("Iterator 1 took {} seconds".format(end_time - start_time))

        chunk_num = 2
        while True:
            try:
                loop_start_time = time.time()
                batch = next(batch_iter)
                chunk = batch.to_pandas()
                chunk.to_sql(name=table_name,  con=engine, if_exists='append', index=False, method='multi')
                loop_end_time = time.time()
                print(f"Iterator {chunk_num} took: {loop_end_time - loop_start_time} seconds")
                chunk_num += 1
            except StopIteration:
                print("Uploading data complete")
                break
            except Exception as e:
                print(f"Error when uploading chunk: {chunk_num}: {e}")
                break
    except StopIteration:
        print("File empty or don't have data")
    except Exception as e:
        print(f"Exception occured: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    # user, password, host, port, db_name, table name, url of the CSV
    parser.add_argument('--user', help='User name for Postgres')
    parser.add_argument('--password', help='Password for Postgres')
    parser.add_argument('--host', help='Host for Postgres')
    parser.add_argument('--port', help='Port for Postgres')
    parser.add_argument('--db', help='Database name for Postgres')
    parser.add_argument('--table_name', help='Name of the table where we will write the results to')
    parser.add_argument('--url', help='URL for file CSV')
    args = parser.parse_args()
    main(args)


