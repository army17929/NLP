# Why do we use API? 
# First, the data is changing quickly.
# Second, there is repeated computation involved.
# What is API? 
# APIs are most commonly used to retrieve data, and that will be thefocus of this beginner tutorial.
import tweepy as tp
import configparser
import requests
# Read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']
print(api_key)

# Authentification 
auth = tp.OAuth1UserHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api = tp.API(auth)

public_tweets = api.home_timeline()
print(public_tweets)