import requests
from datetime import datetime
import os

gender = "male"
weight_kg = "Your weight as number"
height_cm = "Your height as number in cm"
age = "your age as number in years."

API_KEY = "Your api key"
APP_ID = "your api id"
AUTHORIZATION = "string for bearere authentication"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

parameter = {
    'query': input("Explain your exercise: "),
    "gender":gender,
    "weight_kg":weight_kg,
    "height_cm":height_cm,
    "age":age
}

response = requests.post(url=endpoint,json=parameter,headers=headers).json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
sheety_endpoint = "https://api.sheety.co/7a7dd56ebe51ade2f9194e36bd4c7905/workoutTracking/workouts"
bearer_header ={
    "Authorization":f"Bearer {AUTHORIZATION}"
}

for exercise in response["exercises"]:
    sheet_inputs ={
        'workout':{
            "date":today_date,
            "time":now_time,
            "exercise":exercise["user_input"].title(),
            "duration":exercise["duration_min"],
            "calories":exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint,json=sheet_inputs,headers=bearer_header)
    print(sheet_response.status_code)
