from data_processing import show_tb, try_connect_db, save_tb
from twitter_handler import collect_tweets

if __name__ == '__main__':
    # collecting data from twitter 
    collect_tweets()
    # after data colleted try connection to databank
    if try_connect_db() == 'TRUE':
        # if connection works save data in databank 
        save_tb()
        show_tb()
        