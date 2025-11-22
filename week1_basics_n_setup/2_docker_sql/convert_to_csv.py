import pandas as pd

parquet_file_path = '/home/minhnguyen/Documents/DE/data-engineering-zoomcamp/week1_basics_n_setup/2_docker_sql/yellow_tripdata_2021-01.parquet'
df = pd.read_parquet(parquet_file_path)

output_csv_path = '/home/minhnguyen/Documents/DE/data-engineering-zoomcamp/week1_basics_n_setup/2_docker_sql/'
df.to_csv(output_csv_path + 'yellow_tripdata_2021-01.csv', index=False)
print("Conversion from Parquet to CSV completed successfully.")