import os 
import requests

# Nutritionix api
NUTRITIONIZ_APP_ID=os.environ["NUTRITIONIZ_APP_ID"]
NUTRITIONIZ_API_KEY=os.environ["NUTRITIONIZ_API_KEY"]

class Nutritioniz ():
    def __init__(self) -> None:
        pass
    
    def synthesize(self, text: str) -> list:
        nurtritioniz_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
        headers = {"x-app-id": NUTRITIONIZ_APP_ID, "x-app-key": NUTRITIONIZ_API_KEY }
        
        nt_json_data = {"query": text}
        res = requests.post(url=nurtritioniz_endpoint, json=nt_json_data, headers=headers)
        res.raise_for_status()
        return res.json()