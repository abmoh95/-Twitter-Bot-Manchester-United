import tweepy
import time
import BOT_config


# Gainaing access and connecting to Twitter API using Credentials
client = tweepy.Client(bearer_token=BOT_config.BEARER_TOKEN, consumer_key=BOT_config.CONSUMER_KEY,
                       consumer_secret=BOT_config.CONSUMER_SECRET, access_token=BOT_config.ACCESS_KEY, access_token_secret=BOT_config.ACCESS_SECRET)

auth = tweepy.OAuth1UserHandler(
    BOT_config.CONSUMER_KEY, BOT_config.CONSUMER_SECRET, BOT_config.ACCESS_KEY, BOT_config.ACCESS_SECRET)
api = tweepy.API(auth)

search_terms = ["#MUFC"]

# Bot searches for tweets containing certain keywords


class MyStream(tweepy.StreamingClient):

    # This function gets called when the stream is working
    def on_connect(self):
        print("Connected")

    # This function gets called when a tweet passes the stream

    def on_tweet(self, tweet):
        try:
            # Displaying tweet in console
            if tweet.referenced_tweets == None:
                print(tweet.text)
                client.retweet(tweet.id)
                client.like(tweet.id)
                # Delay between tweets
                time.sleep(0.5)
        except Exception as e:
            print(e)

def main():
    try:
        #### Creating Stream object ###
        stream = MyStream(bearer_token=BOT_config.BEARER_TOKEN)
        # A way for the user to test the bot
        rules = tweepy.StreamRule("(from:Twitter_UseruserName) (#testing123 OR Mantest123 United) (-is:reply)")
        stream.add_rules(rules)
        rules1 = tweepy.StreamRule("(from:FabrizioRomano) (#MUFC OR Manchester United OR Man United) (-is:reply)")
        stream.add_rules(rules1)
        print(stream.get_rules())

        ### Delete stream rules based on tweet ID ###
        #stream.delete_rules(ids=[1548360773755289605, 1548356538057703424, 1548003491410374657, 1548006612643696642])

        ### Starting stream ###
        stream.filter()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
