import tweepy

with open('keys_twitter.txt', 'r') as keys:
    consumer_key = keys.readline().strip('\n')
    consumer_secrets = keys.readline().strip('\n')
    access_token = keys.readline().strip('\n')
    access_token_secret = keys.readline().strip('\n')

auth = tweepy.OAuthHandler(consumer_key, consumer_secrets)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

query = '#Ciência' + " -filter:retweets"
tweets = tweepy.Cursor(api.search_tweets,
                        q=query,
                        lang='pt').items(20)

for tweet in tweets:
    print(tweet.text)