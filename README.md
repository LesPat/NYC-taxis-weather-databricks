Project description: Medallion-based architecture data warehouse with data ingestion handled with python by calling NYC yellow taxis free API and meteostat hourly collected weather data for the same period as NYC taxis.

Techstack: AWS S3, Python, API, Databricks (PySpark, SQL), PowerBI

Architecture consists of three layers: Bronze (Staging) -> Silver (Transformation) -> Gold (Business ready)

Python -> S3 -> Databricks -> S3 / PowerBI

<img width="895" height="368" alt="taxis_architecture_draft drawio" src="https://github.com/user-attachments/assets/8379ee33-bbe3-44fd-a124-cb5f1e127d35" />

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
- Adding full area names for analysis
Tables:
- silver_nyc_taxis_weather_oct_dec - joined and cleaned table containing all taxi fares with weather

Gold layer business-ready tables:
- gold.daily_metrics: summarized by date
- gold.hourly_metrics: summarized by hour
- gold.fact_trips: fact table ready for BI
- gold.top_routes: most common trip routes
- gold.weather_impact: analysis of weather on taxi demand
- gold.trip_profitability: profitability per route/time/weather

Business metrics ideas:
- weather vs tips
- distance vs tips
- passangers count vs tips
- tips vs area
- weather vs distance
- time of day vs tips
- ride duration vs tips
