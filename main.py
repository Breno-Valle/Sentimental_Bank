from data_processing import show_tb, try_connect_db, save_tb
from twitter_handler import collect_tweets

if __name__ == '__main__':
    collect_tweets()
    if try_connect_db() == 'TRUE':
        save_tb()
        show_tb()
        