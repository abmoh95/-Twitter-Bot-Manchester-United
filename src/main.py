# Twitter bot

from http import client
import tweepy
import time
import src.config as config

# Del 1
auth = tweepy.OAuthHandler(config.CONSUMER_KEY, config.CONSUMER_SECRET)
auth.set_access_token(config.ACCESS_KEY, config.ACCESS_SECRET)
api = tweepy.Client(bearer_token=config.BEARER_TOKEN)


# query = 'covid'
# solution = api.search_recent_tweets(query=query)
# print(solution.data[0])

# Del 2
client = tweepy.Client(consumer_key=config.CONSUMER_KEY, consumer_secret=config.CONSUMER_SECRET,
                        access_token=config.ACCESS_KEY, access_token_secret=config.ACCESS_SECRET)

# Creating a tweet

#solution = client.create_tweet(text="Hello, Twitter1")
# print(solution)

# Retweet a tweet using its id

#solution1 = client.retweet(tweet_id=1547373906553720833)
# print(solution1)

# Response(data=<User id=330262748 name=Fabrizio Romano username=FabrizioRomano>, includes={}, errors=[], meta={})
id='@FabrizioRomano'
solution = api.get_user(username='FabrizioRomano')
print(solution)
print(solution[0].id)


solution1 = api.get_user(id=config.USER_ID_FABRIZIO)
print(solution1)

solution2 = api.get_users_tweets(id=config.USER_ID_FABRIZIO, max_results=5)

print(solution2.data[0].data['text'])

print(type(solution2))

list_text = []
val = 1
for i in solution2.data:
    print(val,end=' ')
    print(i.id)
    print(i.text)
    list_text.append(i.text)
    val = val+1

for i in list_text:
    if "b" in i:
        print("yes det funkar")

query = '#MUFC'
#solution3 = api.search_recent_tweets(id=config.USER_ID_FABRIZIO, query=query)
#print(type(solution3))
solution2 = api.get_users_tweets(id=config.USER_ID_FABRIZIO, max_results=100)

solution2.data.reverse()
for i in solution2.data:
    if query in i.text:
        print("hejsan123")
        print(i.id)
        print(i.text)
        client.retweet(tweet_id=i.id)
        client.like(tweet_id=i.id)

print(type(solution2.data))



# for i in range(10):
#     print("hello")
#     time.sleep(1)

# try:
#     api.verify_credentials()
#     print("Authentication OK")
# except:
#     print("Error during authentication")


# def main():
#     print("Hello Twitter world, Mancheter United")


# if __name__ == "__main__":
#     main()
