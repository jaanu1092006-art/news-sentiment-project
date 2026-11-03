import streamlit as st
import pandas as pd
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(
    page_title="News Sentiment Dashboard",
    page_icon="📰",
    layout="wide"
)

st.title("📰 News Sentiment Dashboard")
st.write("Latest news and sentiment analysis")

try:
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT")
    )

    query = """
        SELECT title, source_name, published_at,
               sentiment, sentiment_score
        FROM news_articles
        ORDER BY id DESC
    """

    df = pd.read_sql_query(query, connection)
    connection.close()

    st.metric("Total News", len(df))

    if not df.empty:
        col1, col2, col3 = st.columns(3)

        col1.metric("Positive", (df["sentiment"] == "Positive").sum())
        col2.metric("Negative", (df["sentiment"] == "Negative").sum())
        col3.metric("Neutral", (df["sentiment"] == "Neutral").sum())

        st.subheader("Latest News")
        st.dataframe(df, use_container_width=True)

        st.subheader("Sentiment Distribution")
        st.bar_chart(df["sentiment"].value_counts())

    else:
        st.info("No news articles found. Run save_news.py first.")

except Exception as e:
    st.error(f"Database Error: {e}")