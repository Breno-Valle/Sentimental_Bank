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

followers_total = metrics.total_number_followers()
followers_mean = metrics.followers_mean()
followers_stdev = metrics.followers_stdev()
friends_total = metrics.total_number_friends()
friends_mean = metrics.friends_mean()
friends_stdev = metrics.friends_stdev()
day = metrics.day_of_year()

string = f"INSERT INTO {'tb_Stats_Science'} (Followers_total, Followers_mean, Followers_stdev, Friends_total, Friends_mean,Friends_stdev, Time_Of_Query) VALUES ({followers_total}, {followers_mean}, {followers_stdev}, {friends_total}, {friends_mean}, {friends_stdev}, '{day[0]}')"

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-HL3J42P\SQLEXPRESS;'
                      'Database=dbSentimental_Bank;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute(string)
cursor.commit()
cursor.execute('SELECT *  FROM tb_Stats_Science')
print(cursor.fetchall())