# Importing Tweepy and time
import tweepy
import time
import config

# Credentials (INSERT YOUR KEYS AND TOKENS IN THE STRINGS BELOW)
# api_key = ""
# api_secret = ""
# bearer_token = r""
# access_token = ""
# access_token_secret = ""

# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token=config.BEARER_TOKEN, consumer_key=config.CONSUMER_KEY,
                       consumer_secret=config.CONSUMER_SECRET, access_token=config.ACCESS_KEY, access_token_secret=config.ACCESS_SECRET)

auth = tweepy.OAuth1UserHandler(
    config.CONSUMER_KEY, config.CONSUMER_SECRET, config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.API(auth)

search_terms = ["#MUFC"]

# Bot searches for tweets containing certain keywords


class MyStream(tweepy.StreamingClient):

    # This function gets called when the stream is working
    def on_connect(self):

        print("Connected")

    # This function gets called when a tweet passes the stream

    def on_tweet(self, tweet):

        # Displaying tweet in console
        if tweet.referenced_tweets == None:
            print(tweet.text)
            client.retweet(tweet.id)
            client.like(tweet.id)
            # Delay between tweets
            time.sleep(0.5)


#### Creating Stream object ###
stream = MyStream(bearer_token=config.BEARER_TOKEN)

# Adding terms to search rules
# It's important to know that these rules don't get deleted when you stop the
# program, so you'd need to use stream.get_rules() and stream.delete_rules()
# to change them, or you can use the optional parameter to stream.add_rules()
# called dry_run (set it to True, and the rules will get deleted after the bot
# stopped running).

#for i in search_terms:
#stream.add_rules(tweepy.StreamRule(search_terms[0]))

#print(stream.get_rules())
#rules = tweepy.StreamRule("(#MUFC) (@FabrizioUTDBot) (-is:retweet -is:reply)")
#rules = tweepy.StreamRule("(from:FabrizioRomano) (#MUFC) (Manchester United) (-is:reply)")
#rules = tweepy.StreamRule("(from:FabrizioRomano) (#MUFC)")
#stream.add_rules(rules)
rules = tweepy.StreamRule("(from:abdi950329) (#MUFC OR Manchester United) (-is:reply)")
stream.add_rules(rules)
rules1 = tweepy.StreamRule("(from:FabrizioRomano) (#MUFC OR Manchester United) (-is:reply)")
stream.add_rules(rules1)
#stream.add_rules(tweepy.StreamRule(search_terms[0]))


print(stream.get_rules())

### Delete stream rules ###

#stream.delete_rules(ids=[1548360773755289605, 1548356538057703424, 1548003491410374657, 1548006612643696642])


### Starting stream ###

#stream.filter(tweet_fields=["referenced_tweets"])
stream.filter()
