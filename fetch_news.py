import requests
import os

def fetch_news_articles(query):
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={query}&language=en&sortBy=publishedAt&pageSize=5&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()
    print("API Response:", data)
    if data.get("status") != "ok" or not data.get("articles"):
        return []

    return data["articles"]
