import requests

city = input("Enter city name: ")

url = f"https://wttr.in/{city}?format=j1"

response = requests.get(url)

if response.status_code == 200:

    data = response.json()

    temperature = data["current_condition"][0]["temp_C"]
    humidity = data["current_condition"][0]["humidity"]
    weather = data["current_condition"][0]["weatherDesc"][0]["value"]

    print("\nWeather Report")
    print("City:", city)
    print("Temperature:", temperature, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", weather)

else:
    print("Unable to fetch weather data.")