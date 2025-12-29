Project description: Medallion architecture data warehouse with data ingestion handled with python by calling NYC yellow taxis free API and meteostat hourly collected weather data for the same period as NYC taxis. Data uploaded to Amazin S3

Techstack: AWS S3, Python, API, Databricks (PySpark, SQL, Dashboards)

Architecture consists of three layers: Bronze (raw_data ingested from the S3 bucket) -> Silver (Transformation) -> Gold (Business ready)

Python -> S3 -> Databricks -> Databricks Dashboards

<img width="914" height="368" alt="taxis_architecture_v3 drawio" src="https://github.com/user-attachments/assets/5e6cea2e-7cda-430b-ba80-73397c01d2f5" />

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
- silver_nyc_taxis_weather_oct_dec - joined and cleaned table containing all taxi fares with weather with unified naming and added 'technical' columns for aggregations

Gold layer business-ready tables and/or views:
- gold.fact_trips: fact table ready for analysis -> literally silver OBT table (raw table with infinite possibilities) with cleaned and curated bussines-ready data
  
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

  In order to upload result tables into Power BI dashboards databricks <> Power BI connection is needed:
  - Incompatibile format for iOS (solution needed)
  - Databricks native dashboards are sufficient for the analytical purpose
