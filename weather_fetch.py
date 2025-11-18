# Import Meteostat library and dependencies
from datetime import datetime
from meteostat import Point, Hourly
import pandas as pd
import boto3
from io import StringIO

# Set time period
start = datetime(2024, 10, 1)
end = datetime(2024, 12, 31)

# Create Point for New York City, NY
nyc = Point(40.7143, -74.006, 57)

# Get daily data for Oct - Dec 2024
data = Hourly(nyc, start, end)
data = data.fetch()
data = data.reset_index()

# Create CSV in memory
csv_buffer = StringIO()
data.to_csv(csv_buffer, index=False)

s3 = boto3.client(
    "s3"
    #,aws_access_key_id="XXX",
    #aws_secret_access_key="XXX",
    #region_name="eu-north-1"
)

# Upload
s3.put_object(
    Bucket="nyc-taxis-traffic-analysis-raw",
    Key="weather/nyc_weather_oct_dec_2024_v2.csv",
    Body=csv_buffer.getvalue()
)
