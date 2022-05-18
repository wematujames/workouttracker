import os 
import requests
import datetime as dt

# Sheety token
SHEETY_TOKEN= os.environ["SHEETY_TOKEN"]

class Sheety ():
    def __init__(self) -> None:
        pass
    
    def write_record(self, data: dict) -> None:
        sheety_headers = { "Authorization": f"Bearer {SHEETY_TOKEN}" }
        url = "https://api.sheety.co/8b7d51b24d2b637b98d4515e419f2533/myWorkoutsTracker/workouts"
        
        to_save = {
            "workout": {
            "date": dt.datetime.now().strftime("%d/%m/%Y"),
            "time": dt.datetime.now().strftime("%H:%M:%S"),
            "exercise": data["name"].capitalize(),
            "duration": data["duration_min"],
            "calories": data["nf_calories"],
            }
        }
        
        res = requests.post(url=url, json=to_save, headers=sheety_headers)
        res.raise_for_status()
        post_data = res.json()