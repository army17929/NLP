# This is the script that we can label tweets using VADER

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# Load the csv file into a pandas frame.
df = pd.read_csv('tweets(milestone_2000).csv')

# Create an instance of the VADER sentiment analyzer. 
sid = SentimentIntensityAnalyzer()

# Function tolabel sentiment using VADER
def label_sentiment(text):
    sentiment_scores = sid.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return 'Neutral'

print(df['tweets'].head())

# Apply the sentiment labeling function to the text column
df['sentiment_VADER'] = df['tweets'].apply(label_sentiment)

# Save the updated DataFrame to a new csv.file 
df.to_csv('labeled_VADER.csv')