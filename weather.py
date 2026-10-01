import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/weather"

    parameters = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:

        response = requests.get(url, params=parameters)

        data = response.json()

        if response.status_code != 200:

            return "Sorry, I could not find the weather for that location."

        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]

        description = data["weather"][0]["description"]

        return (
            f"The current temperature in {city} is "
            f"{temperature:.1f} degrees Celsius. "
            f"It feels like {feels_like:.1f} degrees. "
            f"The weather is {description}, "
            f"with humidity at {humidity} percent."
        )

    except requests.exceptions.RequestException:

        return "Sorry, I could not connect to the weather service."


if __name__ == "__main__":

    print(get_weather("Pune"))