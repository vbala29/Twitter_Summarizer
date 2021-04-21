# -*- coding: utf-8 -*-
"""deliverable2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1444t59fihWdwAzyViPxrVYJLp6wXK8tz
"""

import csv
import pandas as pd
from operator import itemgetter

def sort_tweets():
  total_csvs = ['#dogecoin.csv','#duantewright.csv','#europeansuperleague.csv','#marshelicopter.csv', '#myanmar.csv','DOYOUNG.csv']
  list_of_dataframes = []
  for filename in total_csvs:
    list_of_dataframes.append(pd.read_csv(filename))
  merged_df = pd.concat(list_of_dataframes)
  merged_df['Like count'] = merged_df['Like count'].astype(int)
  merged_df = merged_df.sort_values(['Hashtag','Like count'], ascending=[True,True])
  merged_df = merged_df.values.tolist()

  return merged_df

sort_tweets()

def tentweet():
  cols = ['Hashtag','tweet1','tweet2','tweet3','tweet4','tweet5','tweet6','tweet7','tweet8','tweet9','tweet10', 'averageLikes']
  strip_tweet = []
  strip_count = 0
  tweets = sort_tweets()
  for x in tweets:
    strip_tweet.append(tweets[strip_count][4])
    strip_count +=1



  rows = []
  r =[]
  counter = 0
  likes = 0
  tweet_count = 0
  for  i in strip_tweet:
    if counter < 10:
      if counter == 0:
        r.append(tweets[tweet_count][0])
      r.append(i)
      likeint = tweets[tweet_count][6]
      likes += likeint
      counter+=1
      tweet_count +=1
      if counter == 10:
        likes = likes/10.0
        r.append(likes) 
    else:
      rows.append(r)
      counter = 0
      likes = 0
      r = []
  with open('tentweetpls1.csv','w') as csvfile:
    writefile= csv.writer(csvfile)
    writefile.writerow(cols)
    writefile.writerows(rows[:200])

tentweet()

def twentytweet():
  cols = ['Hashtag','tweet1','tweet2','tweet3','tweet4','tweet5','tweet6','tweet7','tweet8','tweet9','tweet10','tweet11','tweet12','tweet13','tweet14','tweet15','tweet16','tweet17','tweet18','tweet19','tweet20', 'averageLikes']
  tweets = sort_tweets()
  strip_tweet = []
  strip_count = 0
  for x in tweets:
    strip_tweet.append(tweets[strip_count][4])
    strip_count +=1



  rows = []
  r =[]
  counter = 0
  likes = 0
  tweet_count = 0
  for  i in strip_tweet:
    if counter < 20:
      if counter == 0:
        r.append(tweets[tweet_count][0])
      r.append(i)
      likeint = tweets[tweet_count][6]
      likes += likeint
      counter+=1
      tweet_count +=1
      if counter == 20:
        likes = likes/10.0
        r.append(likes) 
    else:
      rows.append(r)
      counter = 0
      likes = 0
      r = []
  with open('20tweets.csv','w') as csvfile:
    writefile= csv.writer(csvfile)
    writefile.writerow(cols)
    writefile.writerows(rows[:200])

twentytweet()

def notweet():
  tweets = sort_tweets()
  strip_tweet = []
  strip_count = 0
  for x in tweets:
    strip_tweet.append(tweets[strip_count][0])
    strip_count +=1
  rows = []
  r =[]
  counter = 0
  tweet_count = 0
  for  i in strip_tweet:
    if counter < 10:
      r.append(i)
      counter+=1
    else:
      rows.append(r)
      counter = 0
      r = []
  with open('notweets.csv','w') as csvfile:
    writefile= csv.writer(csvfile)
    writefile.writerow(cols)
    writefile.writerows(rows[:200])

notweet()