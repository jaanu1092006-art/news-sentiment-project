import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get NewsData API Key
API_KEY = os.getenv("NEWSDATA_API_KEY")

if not API_KEY:
    raise ValueError("NEWSDATA_API_KEY not found in .env file")

# NewsData API URL
url = "https://newsdata.io/api/1/latest"

# API Parameters
params = {
    "apikey": API_KEY,
    "language": "en"
}

# Fetch news articles
print("Starting News Collector...")

try:
    response = requests.get(url, params=params, timeout=20)

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("API Error:", response.text)
        response.raise_for_status()

    data = response.json()

    articles = data.get("results", [])

    print(f"Fetched {len(articles)} articles.")

    # Display news articles
    for article in articles:
        print("-----------------------------")
        print("Title:", article.get("title"))
        print("Source:", article.get("source_id"))
        print("Description:", article.get("description"))
        print("Published At:", article.get("pubDate"))
        print("URL:", article.get("link"))

except requests.exceptions.RequestException as e:
    print("Error fetching news:", e)