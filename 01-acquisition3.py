import tweepy
import json

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.num_tweets = 0
        self.file = open("tweets.txt", "w")

    def on_status(self, status):
        tweet = status._json
        print(self.num_tweets)
        print(tweet)
        self.file.write(json.dumps(tweet) + '\n' )
        self.num_tweets += 1
        if self.num_tweets < 10:
            return True
        else:
            return False
        self.file.close()

    def on_error(self, status):
        print(status)

l = MyStreamListener()

# Create you Stream object with authentication
stream = tweepy.Stream(auth, l)

# Filter Twitter Streams to capture data by the keywords:
#stream.filter(locations=[-74.0231,45.3299,-73.3846,45.7311],track=['clinton','trump','sanders','cruz'])
stream.filter(track=['basketball'])

import json

# String of path to file: tweets_data_path
tweets_data_path='tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data=[]

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet=json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())

tweets_data[9]

import pandas as pd

# Build DataFrame of tweet texts and languages
df = pd.DataFrame(tweets_data, columns=['text','lang','user'])

# Print head of DataFrame
print(df.head())

df.to_csv('data/tweets.csv')