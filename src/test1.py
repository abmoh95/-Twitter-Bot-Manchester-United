def main():
  import tweepy
  import time
  import config


  client = tweepy.Client(bearer_token=config.BEARER_TOKEN, consumer_key=config.CONSUMER_KEY,
                       consumer_secret=config.CONSUMER_SECRET, access_token=config.ACCESS_KEY, access_token_secret=config.ACCESS_SECRET)

  auth = tweepy.OAuth1UserHandler(
            config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_KEY, config.ACCESS_SECRET)
  api = tweepy.API(auth)

  search_terms = ["#MUFC"]



  class MyStream(tweepy.StreamingClient):

    def on_connect(self):

      print("Connected")


    def on_tweet(self, tweet):

      if tweet.referenced_tweets == None:
        print(tweet.text)
        client.retweet(tweet.id)
        client.like(tweet.id)
        time.sleep(0.5)


  stream = MyStream(bearer_token=config.BEARER_TOKEN)


  rules = tweepy.StreamRule("(from:FabrizioRomano) (#MUFC) (Manchester United) (-is:reply)")

  stream.add_rules(rules)

  print(stream.get_rules())

  stream.filter()