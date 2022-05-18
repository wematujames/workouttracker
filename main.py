import datetime as dt
import requests
import os

# Nutritionix api
NUTRITIONIZ_APP_ID=os.environ["NUTRITIONIZ_APP_ID"]
NUTRITIONIZ_API_KEY=os.environ["NUTRITIONIZ_API_KEY"]

# Sheety token
SHEETY_TOKEN= os.environ["SHEETY_TOKEN"]


nurtritioniz_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {"x-app-id": NUTRITIONIZ_APP_ID, "x-app-key": NUTRITIONIZ_API_KEY }
nt_json_data = {"query": "Ran 5k and jumping jacks for 25 minutes"}
res = requests.post(url=nurtritioniz_endpoint, json=nt_json_data, headers=headers)
res.raise_for_status()
data = res.json()


# Get rows, insert row on sheety
sheety_headers = { "Authorization": f"Bearer {SHEETY_TOKEN}" }

url = "https://api.sheety.co/8b7d51b24d2b637b98d4515e419f2533/myWorkoutsTracker/workouts"
for exercise in data["exercises"]:
    to_save = {
        "workout": {
        "date": dt.datetime.now().strftime("%d/%m/%Y"),
        "time": dt.datetime.now().strftime("%H:%M:%S"),
        "exercise": exercise["name"].capitalize(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
        }
    }
    res = requests.post(url=url, json=to_save, headers=sheety_headers)
    res.raise_for_status()
    post_data = res.json()




