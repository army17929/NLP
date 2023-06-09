# APIs are most commonly used to retrieve data, and that will be thefocus of this beginner tutorial.
import tweepy as tp
import configparser
import requests
import pandas as pd 

# Read configs
config = configparser.ConfigParser()
config.read(r"C:\Users\every\OneDrive\NLP_project\Tweeter_streaming\streaming\config.ini")

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# Authentification 
auth = tp.OAuth1UserHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)
bear = 'AAAAAAAAAAAAAAAAAAAAAApGmwEAAAAA0hwdTR1gQ63tHNb8e2uAfSuIEug%3DcY5XCQemELs7QesJ28iOzgTXbW6WTy6Mo2aNMev66bOcaDIaPh'

client = tp.Client(bearer_token=bear)
api = tp.API(auth)

keyword = 'nuclear'
count = 1 
result = []
while (count<=2):
    tweets = client.search_recent_tweets(keyword,max_results = 10)
    for tweet in tweets:
        result.append(tweet)
    count += 1
print(result)

import csv 

with open('list_to_csv.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(result)

original_file = r'C:\Users\every\OneDrive\바탕 화면\Github\NLP\data_collection\data_collected.csv'
#df = pd.read_csv(original_file,encoding='utf-8',error_bad_lines = False)
#data = df['text']
#print(data.head())