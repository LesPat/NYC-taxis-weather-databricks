Project description: Medallion-based architecture data warehouse with data ingestion handled with python by calling NYC yellow taxis free API and meteostat hourly collected weather data for the same period as NYC taxis.

Techstack: AWS S3, Python, API, Databricks (PySpark, SQL), PowerBI

Architecture consists of three layers: Bronze (Staging) -> Silver (Transformation) -> Gold (Business ready)

<img width="794" height="368" alt="taxis_architecture_draft drawio" src="https://github.com/user-attachments/assets/ac9ce806-97f7-4934-b0cc-370553934450" />

NYC yellow taxis data reference: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

Weather data reference: https://dev.meteostat.net/python/

Python -> S3 -> Databricks -> S3 / PowerBI

Business metrics idea:
- weather vs tips
- distance vs tips
- passangers count vs tips
- tips vs area
