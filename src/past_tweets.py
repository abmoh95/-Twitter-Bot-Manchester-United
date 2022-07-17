# Twitter bot

import tweepy
import time
import src.config as config

# PART 1
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.Client(bearer_token=config.BEARER_TOKEN)

# PART 2
client = tweepy.Client(consumer_key=config.CONSUMER_KEY, consumer_secret=config.CONSUMER_SECRET,
                        access_token=config.ACCESS_KEY, access_token_secret=config.ACCESS_SECRET)

#### This is how you creat a tweet ###

# solution = client.create_tweet(text="Hello, Twitter")
# print(solution)

### Retweet a tweet using its id ###

# solution1 = client.retweet(tweet_id=1547373906553720833)
# print(solution1)

# Response(data=<User id=330262748 name=Fabrizio Romano username=FabrizioRomano>, includes={}, errors=[], meta={})
username='@FabrizioRomano'
info_Fab = api.get_user(username='FabrizioRomano')
print(info_Fab)
print(info_Fab[0].username)


Past_Tweets_Fab = api.get_users_tweets(id=config.USER_ID_FABRIZIO, max_results=5)

print(Past_Tweets_Fab.data[0].data['text'])

print(type(Past_Tweets_Fab))

list_text = []
val = 1
for i in Past_Tweets_Fab.data:
    print(val,end=' ')
    print(i.id)
    print(i.text)
    list_text.append(i.text)
    val = val+1


### Search through the past 100 tweets from Fabrizio that matches the hastag. If we find tweets
### that matches our hashtag then we retweet it as well as like it. 
query = '#MUFC'
Past_Tweets_Fab = api.get_users_tweets(id=config.USER_ID_FABRIZIO, max_results=100)

Past_Tweets_Fab.data.reverse()
for i in Past_Tweets_Fab.data:
    if query in i.text:
        print(i.id)
        print(i.text)
        client.retweet(tweet_id=i.id)
        client.like(tweet_id=i.id)

print(type(Past_Tweets_Fab.data))

