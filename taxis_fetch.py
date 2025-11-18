import requests
import os
import boto3

urls = ['https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2024-12.parquet']

local_dir = '/tmp/parquet_files'
bucket_name = 'nyc-taxis-traffic-analysis-raw'

os.makedirs(local_dir, exist_ok=True)
s3 = boto3.client(
    "s3"
    #,aws_access_key_id="XXX",
    #aws_secret_access_key="XXX",
    #region_name="eu-north-1"
)

for url in urls:
    filename = url.split("/")[-1]
    local_path = os.path.join(local_dir, filename)
    s3_key = f"{filename}"

    with requests.get(url, stream = True) as r:
        with open(local_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192*8):
                f.write(chunk)
    
    s3.upload_file(local_path, bucket_name, s3_key)
