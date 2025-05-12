import requests
import datetime as dt

date_today=dt.datetime.now().strftime("%d/%m/%Y")
time_now=dt.datetime.now().strftime("%X")

#------------Keys and Endpoint-------------------#

APP_ID="3bc602a8"
API_KEY="2f698a6c14ab9b99b06e7e20ac9ddede"
REQUEST_ENDPOINT="https://trackapi.nutritionix.com/v2/natural/exercise"
SHEET_ENDPOINT="https://api.sheety.co/d9d4dedfcb2cc2cb97f8cf8fc0af4134/workoutTracking/workouts"

input_user=input("Enter the Excercise You did and the duration")

#-------------------- Header and Parameter for Nutritionix--------------------#

headers={
    "x-app-id":APP_ID,
    "x-app-key":API_KEY

}
parameters = {
    "query": input_user
}

#-----------------Getting Response and Going Through the json Data --------------------------#

response=requests.post(REQUEST_ENDPOINT,json=parameters,headers=headers)
data=response.json()
workout=data["exercises"]
for i in range(0,len(workout)):
    #-----------------Parameter Body for Sheety-----------------#
    body={
    "workout":
    {
        "date": date_today,
            "time": time_now,
            "exercise": workout[i]["name"],
            "duration": workout[i]["duration_min"],
            "calories": workout[i]["nf_calories"]
    }

    }
    sheet_response=requests.post(SHEET_ENDPOINT,json=body)
    print(sheet_response.json())




