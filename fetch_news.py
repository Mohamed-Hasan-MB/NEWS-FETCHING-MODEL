import requests
import os
import urllib.parse

def fetch_news_articles(query):
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")

    if not NEWS_API_KEY:
        print("ERROR: NEWS_API_KEY not found in environment variables.")
        return []

    encoded_query = urllib.parse.quote(query)
    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={encoded_query}&language=en&sortBy=publishedAt&pageSize=5&page=1&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)
    data = response.json()
    print("API Response:", data)

    if data.get("status") != "ok" or not data.get("articles"):
        return []

    return data["articles"]
