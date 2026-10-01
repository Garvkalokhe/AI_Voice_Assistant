import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("NEWS_API_KEY")


def get_news():

    url = "https://newsapi.org/v2/top-headlines"

    parameters = {
        "country": "us",
        "apiKey": API_KEY,
        "pageSize": 5
    }

    try:

        response = requests.get(url, params=parameters)

        data = response.json()

        if response.status_code != 200:

            return ["Sorry, I could not fetch the latest news."]

        articles = data.get("articles", [])

        headlines = []

        for article in articles:

            title = article.get("title")

            if title:
                headlines.append(title)

        if not headlines:

            return ["Sorry, there are no news headlines available right now."]

        return headlines

    except requests.exceptions.RequestException:

        return ["Sorry, I could not connect to the news service."]
