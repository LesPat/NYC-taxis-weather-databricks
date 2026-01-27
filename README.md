Project description: Medallion architecture data warehouse with data ingestion handled with python by calling NYC yellow taxis free API and meteostat hourly collected weather data for the same period as NYC taxis. Data uploaded to Amazon S3.

Techstack: AWS S3, Python, API, Databricks (PySpark, SQL, DAB, LDP, Jobs)

Architecture consists of three layers: Bronze (raw_data ingested from the S3 bucket) -> Silver (Transformation) -> Gold (Business ready)

Python -> S3 -> Databricks

![taxis_architecture_draft_v2](https://github.com/user-attachments/assets/b7f27286-177e-4bc5-8c32-91ad5b342cde)

References:
NYC yellow taxis data: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
Weather data: https://dev.meteostat.net/python/

Bronze layer tables:
1. bronze_nyc_taxis_oct_dec_2024
   Contains NYC yellow taxis fares from period of Oct '24 to Dec '24
2. bronze_taxi_zone_lookup
   Contains dictionary for NYC districts abbreviations
3. bronze_weather_oct_dec_2024
   Contains weather for NYC from period of Oct '24 to Dec '24

Silver layer transformations and result tables:
- Deleting records with irrelevant data (dates out of scope)
- Joining NYC fares data with weather (date_trunc to full hours = hourly weather data)
- Adding full area names for analysis.
Tables:
- silver_nyc_taxis_weather_oct_dec - joined and cleaned table containing all taxi fares with weather with unified naming and added 'technical' columns for aggregations. Plan to create Airflow orchestrated synthetic data ingestion to hands-on learn about AutoLoader feature.

Gold layer business-ready tables and/or views:
- gold.fact_trips: fact table ready for analysis -> literally silver OBT table (raw table with infinite possibilities) with cleaned and curated bussines-ready data.
  
- gold.daily_metrics: grouped by date -> metrics:
   +total (avg, min, max, sum)
   +fare (avg, min, max, sum)
   +tips (avg, min, max, sum) 
   +duration (avg, min, max)
   +weather (avg rain, total rain, avg temp, avg wind)
   +distance (avg, min, max)
  
- gold.hourly_metrics: grouped by hour -> metrics:
   +total(avg, min, max, sum)
   +fare(avg, min, max, sum)
   +tips(avg, min, max, sum) 
   +duration (avg, min, max)
   +weather(avg rain, total rain, avg temp, avg wind)
   +distance (avg, min, max)
  
- gold.dayofweek_metrics: summarized by day of week -> 
   +total(avg, min, max, sum)
   +fare(avg, min, max, sum)
   +tips(avg, min, max, sum) 
   +duration (avg, min, max)
   +distance (avg, min, max)
  
- gold.weather_impact: analysis of weather on taxi demand ->
   +fares count
   +total(avg, min, max, sum)
   +fare(avg, min, max, sum)
   +tips(avg, min, max, sum) 
   +duration (avg, min, max)
   +profitability (total/duration, total/distance)
   +distance (avg, min, max)
  
- gold.top_routes: grouped by top routes (sorted by count) -> metrics:
   +total(avg, min, max, sum)
   +fare(avg, min, max, sum)
   +tips(avg, min, max, sum) 
   +duration (avg, min, max)
   +profitability (total/duration, total/distance)
   +distance (avg, min, max)

Project is planned to be refactored into Lakeflow Declarative Pipeline and will be archived afterward.

Some unecessary columns are to be deleted. Joins being relocated to silver-to-gold step, data cleaning will be applied in bronze-to-silver step. DAB will be leveraged in order to implement CI/CD features. Synthetic data generator will be implemented in order to test AutoLoader capabilities. Transformation will be handled with LDP in DAB.
