# This script enables us to collect unlimited tweets from the tweeter
# But this is not for the live streaming, just for collecting the data.
import snscrape.modules.twitter as sntwitter
import pandas as pd
import os 
import sklearn as skl

dir = r'C:\Users\every\OneDrive\NLP_project\Sentiment_analysis\NLP\data_collection'
os.chdir(dir)

query = "nuclear"
tweets = []
limit = 100

for tweet in sntwitter.TwitterSearchScraper(query).get_items():
    #print(vars(tweet))
    #break
    if len(tweets) == limit :
        break
    else:
        tweets.append([tweet.date,tweet.content])
    df = pd.DataFrame(tweets,columns=['Date','Tweet'])
df.to_csv('data.csv')