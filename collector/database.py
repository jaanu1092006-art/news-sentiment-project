import psycopg2

def get_connection():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="news_sentiment_db",
            user="postgres",
            password="root",
            port="5432"
        )

        print("PostgreSQL Connected Successfully!")
        return connection

    except Exception as e:
        print("Database Connection Error:", e)
        return None


if __name__ == "__main__":
    connection = get_connection()

    if connection:
        connection.close()
        print("Database Connection Closed.")