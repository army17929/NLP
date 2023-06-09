from textblob import TextBlob
import pandas as pd

# Read the csv file into a dataframe
df = pd.read_csv(r'C:\Users\every\OneDrive\바탕 화면\Github\NLP\data_collection\dropped_duplicates.csv')

# Define a function to apply textblob sentiment analysis to each row.
def get_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity
    if sentiment_score > 0.0:
        sentiment = "Positive"
    elif sentiment_score < 0.0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    return sentiment
# Apply the sentiment analysis function to the tweets column and create a new sentimnet column
df['sentiment'] = df['tweets'].apply(get_sentiment)

# Print the results
print(df.head())