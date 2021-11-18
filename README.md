# Sentimental_Bank
Find and Save and Process  tweets using pyspark and Structured DataBank

OBJECTIVE:

Build an ETl file that can menage data from Twitter and save it to analyse how much direct followers, and friends wer impacted by the use of an espefic Hashtag. On this case, i used the key word "Ciencia" (that means Science in portuguese) and understand how it varies in time, givin data to relationate with new descoveries, social movements or political actions hhat have some relation with Science.

My main goal here is understand the direct impact of an use of this Hashtag, measuring how much people were exposed to that theme. SO i was worried to save:

- followers_total
- followers_mean
- followers_stdev
- friends_total
- friends_mean
- friends_stdev
- day
Tweet's content were not comtemplated here, only numerical data

FUTURE PLANS:

My future plans to this project are related to NLP and tweet's content, to have a deeper understanding of the people's fellings and thoughts about this topic. I also want to extend the number of topics to be add, adding new Key words (Hashtags) to search and save.

WHAT'S NEXT?

After this ETL processing, i will build an Tableau graphic and connect it to my portifolio website, allowing non IT people to extract meaning from this topic, without using SQL.

WHAT WAS USED ON THIS PROJECT?

PYTHON 3.8
- findspark
- pyspark
- pickle
- pyodbc
- tweepy
- spark-3.1.1-bin-hadoop2.7
MICROSOFT SQL SERVER 2019
