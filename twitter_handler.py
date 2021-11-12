#import tweepy for twitter's API and Menagement
import tweepy
#import pickle to load structured data into a file
import pickle

# consume twitter login keys from a txt file
with open('files\keys_twitter.txt', 'r') as keys:
    consumer_key = keys.readline().strip('\n')
    consumer_secrets = keys.readline().strip('\n')
    access_token = keys.readline().strip('\n')
    access_token_secret = keys.readline().strip('\n')


def collect_tweets():
    try:
        # starting authencartion on the API's connection
        auth = tweepy.OAuthHandler(consumer_key, consumer_secrets)
        auth.set_access_token(access_token, access_token_secret)

        #instatiate twitter API menager 
        api = tweepy.API(auth)
        try: 
            #query an especific word without retweets
            query = '#Ciência' + " -filter:retweets"
            # save all tweets into tweets variable using api class
            tweets = tweepy.Cursor(api.search_tweets,
                                    q=query,
                                        tweet_mode='extended',
                                    lang='pt').items(30000)


            # saving data from tweets into a dictionary and than into an binary file
            with open('files\arquivo', 'w+b') as arq:
                # creating an dict
                tw_dict ={'date': [], 'text': [], 'number_followers':[], 'number_friends':[], 'location':[]}
                # loop over tweets and get their atributes
                for tweet in tweets:
                    text = tweet.full_text.encode('utf-8')
                    date = str(tweet.created_at).encode('utf-8')
                    number_followers = str(tweet.user._json["followers_count"]).encode('utf-8')
                    number_friends = str(tweet.user._json["friends_count"]).encode('utf-8')
                    location = str(tweet.user._json['location']).encode('utf-8')
                    tw_dict['date'].append(date)
                    tw_dict['text'].append(text)
                    tw_dict['number_followers'].append(number_followers)
                    tw_dict['number_friends'].append(number_friends)
                    tw_dict['location'].append(location)
                #load dict into an binary file
                pickle.dump(tw_dict, arq)
        except:
            print('Unable to collect data')
    except:
        print('Connection failed')


