import findspark
findspark.init()
import pyspark as ps
import pickle
import pyodbc

spark = ps.sql.SparkSession.builder \
        .master('local[1]') \
        .appName('Sentimental-bank-processing') \
        .getOrCreate()
sc = spark.sparkContext  

path = r'C:\Users\Breno\Documents\ComputerScience\sentimental_bank\arquivo'

with open(path, 'rb') as arq:
    tw_dict = pickle.load(arq)

class Find_Metrics:
    def __init__(self, dict):
        self.dict = dict
        self.number_followers = [number for number in tw_dict['number_followers']]
        self.date = [day for day in tw_dict['date']]
        self.number_friends = [n_friends for n_friends in tw_dict['number_friends']]
        self.location = [local for local in tw_dict['location']]
        
    def total_number_followers(self):
        total = sc.parallelize(self.number_followers) \
                .map(lambda x: int(x)) \
                .sum()
        return total
    
    def followers_mean(self):
        mean = sc.parallelize(self.number_followers) \
                .map(lambda x: int(x)) \
                .mean()
        return mean
    
    def followers_stdev(self):
        stdev = sc.parallelize(self.number_followers) \
                .map(lambda x: int(x)) \
                .stdev()
        return stdev
    
    def total_number_friends(self):
        total = sc.parallelize(self.number_friends) \
                .map(lambda x: int(x)) \
                .sum()
        return total
    
    def friends_mean(self):
        mean = sc.parallelize(self.number_friends) \
                .map(lambda x: int(x)) \
                .mean()
        return mean
    
    def friends_stdev(self):
        stdev = sc.parallelize(self.number_friends) \
                .map(lambda x: int(x)) \
                .stdev()
        return stdev
    
    def day_of_year(self):
        day = sc.parallelize(self.date) \
                .map(lambda x: x.decode('utf-8')[0:10]) \
                .take(1)
        return day
    
    def city(self):
        loc = sc.parallelize(self.location) \
                .map(lambda x: x.decode('utf-8').lower()) \
                .filter(lambda x: x != '') \
                .collect()
        return loc

metrics =  Find_Metrics(tw_dict)

followers_total = round(metrics.total_number_followers(), 4)
followers_mean = round(metrics.followers_mean(), 4)
followers_stdev = round(metrics.followers_stdev(), 4)
friends_total = round(metrics.total_number_friends(),4)
friends_mean = round(metrics.friends_mean(),4)
friends_stdev = round(metrics.friends_stdev(),4)
day = metrics.day_of_year()


class Query:
    def __init__(self, table_name):
        self.create_table = "CREATE TABLE {table_name} (Query_id INT IDENTITY(1,1) PRIMARY KEY, Followers_total INT, Followers_mean FLOAT, Followers_stdev FLOAT, Friends_total INT, Friends_mean FLOAT, Friends_stdev FLOAT)"
        self.save = f"INSERT INTO {table_name} (Followers_total, Followers_mean, Followers_stdev, Friends_total, Friends_mean,Friends_stdev, Time_Of_Query) VALUES ({followers_total}, {followers_mean}, {followers_stdev}, {friends_total}, {friends_mean}, {friends_stdev}, '{day[0]}')"
        self.see_all = f"SELECT *  FROM {table_name}"


def try_connect_db():
    try:
        conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-HL3J42P\SQLEXPRESS;'
                              'Database=dbSentimental_Bank;'
                              'Trusted_Connection=yes;')

        cursor = conn.cursor()
        try:
            cursor.execute(Query('tb_Stats_Science').see_all)
            cursor.fetchone()
            cursor.close()
            return 'TRUE'
        except:
            print('Table does not exists')
    except:
        print('Unable to connet with requested database')


def save_tb():
    conn = pyodbc.connect('Driver={SQL Server};'
                              'Server=DESKTOP-HL3J42P\SQLEXPRESS;'
                              'Database=dbSentimental_Bank;'
                              'Trusted_Connection=yes;')
    cursor = conn.cursor()
    cursor.execute(Query('tb_Stats_Science').save)
    cursor.commit()
    cursor.close()


