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

# Define a custom StreamListener to handle incoming tweets
class MyStreamListener(tp.StreamListener):
    def on_status(self, status):
        print(f"Tweet: {status.text}")

# Create an instance of the custom StreamListener
my_stream_listener = MyStreamListener()

# Create a streaming object using the API and the custom StreamListener
my_stream = tp.Stream(auth=api.auth, listener=my_stream_listener)

# Filter the stream for tweets containing "nuclear power"
my_stream.filter(track=["nuclear power"])

'''
import csv 

with open('list_to_csv.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(result)
'''