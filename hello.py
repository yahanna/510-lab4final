import schedule
import time
from data import fetch_and_store_weather_data  

api_key = "d1bdfd06881bbff02296606bc8a6ce9b"  
cities = [("London", "UK"), ("Paris", "France"), ("Berlin", "Germany")]  

def scheduled_job():
    for city_name, country in cities:
        fetch_and_store_weather_data(api_key, city_name, country)
        print(f"Data fetched for {city_name}, {country}")

schedule.every(30).minutes.do(scheduled_job)

while True:
    schedule.run_pending()
    time.sleep(1)