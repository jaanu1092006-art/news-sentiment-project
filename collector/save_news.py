import os
import requests
import psycopg2
from dotenv import load_dotenv
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

load_dotenv()

API_KEY = os.getenv("NEWSDATA_API_KEY")

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    scores = analyzer.polarity_scores(text or "")
    score = scores["compound"]

    if score >= 0.05:
        sentiment = "Positive"
    elif score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, score


def save_news():
    connection = None

    try:
        # Connect to PostgreSQL
        connection = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT")
        )

        cursor = connection.cursor()

        # Fetch news from NewsData.io
        url = "https://newsdata.io/api/1/latest"
        params = {
            "apikey": API_KEY,
            "language": "en"
        }

        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()

        articles = response.json().get("results", [])

        print("Fetched articles:", len(articles))

        for article in articles:
            title = article.get("title") or ""
            description = article.get("description") or ""
            text = title + " " + description

            sentiment, score = analyze_sentiment(text)

            cursor.execute("""
                INSERT INTO news_articles
                (title, source_name, description, published_at,
                 sentiment, sentiment_score, url)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (url) DO NOTHING
            """, (
                title,
                article.get("source_id"),
                description,
                article.get("pubDate"),
                sentiment,
                score,
                article.get("link")
            ))

        connection.commit()
        print("News saved successfully!")

    except Exception as e:
        print("Error:", e)

        if connection:
            connection.rollback()

    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    save_news()