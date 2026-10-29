from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create sentiment analyzer
analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):

    if not text:
        return "Neutral", 0.0

    # Analyze the text
    scores = analyzer.polarity_scores(text)

    compound_score = scores["compound"]

    # Classify sentiment
    if compound_score >= 0.05:
        sentiment = "Positive"

    elif compound_score <= -0.05:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    return sentiment, compound_score


# Test sentiment analysis
if __name__ == "__main__":

    news = "The company achieved record profits this year"

    sentiment, score = analyze_sentiment(news)

    print("News:", news)
    print("Sentiment:", sentiment)
    print("Score:", score)