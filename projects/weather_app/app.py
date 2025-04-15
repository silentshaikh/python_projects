import requests
import os
from dotenv import load_dotenv


apiKey = os.getenv("APIKEY")
inputForCity = input("Enter the name of your city : ")
if inputForCity or apiKey:
    apiUrl = f"https://api.openweathermap.org/data/2.5/weather?q={inputForCity}&units=metric&appid={apiKey}"
    getResponse = requests.get(apiUrl).json()
    load_dotenv()
    print(getResponse)
else:
    print("Missing Api key or City Name")