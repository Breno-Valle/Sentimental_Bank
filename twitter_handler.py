import tweepy
import pickle
from os.path import exists

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
                        tweet_mode='extended',
                        lang='pt').items(6)



with open('arquivo', 'w+b') as arq:
    tw_dict ={'date': [], 'text': [], 'number_followers':[]}
    for tweet in tweets:
        text = tweet.full_text.encode('utf-8')
        date = str(tweet.created_at).encode('utf-8')
        number_followers= str(tweet.user._json["followers_count"]).encode('utf-8')
        tw_dict['date'].append(date)
        tw_dict['text'].append(text)
        tw_dict['number_followers'].append(number_followers)
    pickle.dump(tw_dict, arq)

     



