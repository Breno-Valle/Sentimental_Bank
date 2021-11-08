from data_processing import Find_Metrics, Query, try_connect_db, save_tb
from twitter_handler import collect_tweets

if __name__ == '__main__':
    collect_tweets()
    if try_connect_db() == 'TRUE':
        save_tb()
        print('Boa')
        