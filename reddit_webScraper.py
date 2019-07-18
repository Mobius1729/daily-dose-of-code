#!/usr/bin/env python
# coding: utf-8

# In[71]:


import praw
import datetime as dt
import json
import csv

#initalize praw
reddit = praw.Reddit(client_id='4hqdHPpJDAGsJg',                      
                     client_secret='O8Qirn8FgGUNi55Mh_Us4_Mqtls',                      
                     user_agent='ProgrammerHumor Web Scraper',                      
                     username='***********',                      
                     password='***********')

#get subreddit (r/DailyProgrammer)
subreddit = reddit.subreddit('DailyProgrammer')

#sort the subreddit by hot
sort_hot_subreddit = subreddit.hot(limit = (26))

#all the elemnts of the post we wish to get
topics_dict = {"title": [],               
               "score" : [],               
               "id" : [],               
               "numOfComments" : [],               
               "created": [],               
               "body" : [],               
               "upvotes" : [],
              "flair" : []}

#append elements from post to apropriate lists.
for submission in sort_hot_subreddit:
    topics_dict["title"].append(submission.title)
    topics_dict["score"].append(submission.score)
    topics_dict["id"].append(submission.id)
    topics_dict["numOfComments"].append(submission.num_comments)
    topics_dict["created"].append(submission.created)
    topics_dict["body"].append(submission.selftext)
    topics_dict["upvotes"].append(submission.upvote_ratio)
    topics_dict["flair"].append(submission.link_flair_text)


data_to_csv = topics_data.to_csv('programmingChallenges_reddit.csv', index = False) #convert data to a CSV file
json_str = json.dumps(topics_dict).encode('utf-8') #convert data to a JSON file
json_str_prettyPrint = json.dumps(topics_dict, sort_keys = True, indent = 2, separators=("\n", ";")) #set JSON to pretty printing

#write contents to JSON file
with open('json_str.json', 'w') as outfile:
    json.dump(topics_dict, outfile)

print(json_str_prettyPrint)
