# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 16:46:52 2020

@author: amita80039...174510
"""
import asyncio
import twint
import nest_asyncio
import pandas
import pyreadr
import os
import datetime 
from dateutil.relativedelta import relativedelta
import time
os.environ["R_HOME"] = r"D:\Program Files\R\R-4.0.2"
os.environ["PATH"]   = r"D:\Program Files\R\R-4.0.2\bin\x64" + ";" + os.environ["PATH"]
import rpy2

import rpy2.robjects as robjects
from rpy2.robjects import pandas2ri
pandas2ri.activate()

readRDS = robjects.r['readRDS']
df = readRDS(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later.Rds")
df=df[95336:100000]
slice2=df[10001:20000]
slice3=df[20001:30000]
slice4=df[30001:40000]
slice5=df[40001:50000]
slice6=df[50001:60000]
slice7=df[60001:70000]
slice8=df[70001:80000]
slice9=df[80001:90000]
slice10=df[90000:100000]
slice11=df[100001:110000]
slice12=df[110001:120000]
slice12=df[120001:130000]
slice13=df[130001:140000]
slice14=df[140001:150000]
slice15=df[150001:160000]
slice16=df[160001:170000]
slice17=df[170001:180000]
slice18=df[180001:190000]
slice19=df[190001:193839]




nest_asyncio.apply()



later = df[df['conversation_id']==0]


for index, row in slice1.iterrows():
    for i in range(1,8):
        nest_asyncio.apply()
        replies = twint.Config()
        replies.Pandas = True
        replies.To = "@" + row['username']
        replies.Until = (datetime.datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S")+ relativedelta(days=8-i)).strftime("%Y-%m-%d")
        replies.Since = (datetime.datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S")+ relativedelta(days=7-i)).strftime("%Y-%m-%d")
        twint.run.Search(replies)
        repliesdf = twint.storage.panda.Tweets_df
        #test = replies[replies['conversation_id']==row['id']]
        if len(repliesdf)>0:
            frames = [shamelater, repliesdf[repliesdf['conversation_id']==row['id']]]
            shamelater = pandas.concat(frames)





replies = twint.storage.panda.Tweets_df

test = replies[replies['conversation_id']=="1335766709748310017"]



##helpfrom tal
for index, row in df.head(n=2).iterrows():
    replies = twint.Config()
    replies.Pandas = True
    replies.To = "@" + row['username']
    replies.Until = (datetime.datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S")+ relativedelta(weeks=1)).strftime("%Y-%m-%d")
    replies.Since = (datetime.datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S")- relativedelta(days=1)).strftime("%Y-%m-%d")
    print(replies.To)
    print(replies.Until)
    print(replies.Since)


datetime.strptime()
datetime.datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S")
six_months = date.today() + relativedelta(months=6)
    replies.Pandas = True


######replies

for index, row in df.iterrows():
    start_str = (datetime.datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S")- relativedelta(days=1)).strftime("%Y-%m-%d")
    end_str = (datetime.datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S")+ relativedelta(weeks=1)).strftime("%Y-%m-%d")
    start_date = pandas.to_datetime(start_str, format='%Y-%m-%d', errors='ignore')
    end_date = pandas.to_datetime(end_str, format='%Y-%m-%d', errors='ignore')
    data_folder = "D:/Users/amita/Desktop/social psychology/thesis/code/data/"
    resume_file = r"{data_folder}resume.txt"
    replies = twint.Config()
    replies.To = row['username']
    replies.Resume = resume_file
    replies.Pandas = True
    
    while start_date < end_date:
     
        check = 0
        replies.Since = datetime.datetime.strftime(start_date, format='%Y-%m-%d')
        replies.Until = datetime.datetime.strftime(start_date + relativedelta(days=1), format='%Y-%m-%d')
    
        while check < 1:
            try:
                print("Running Search: Check ", start_date)
                twint.run.Search(replies)
                searched=True
                check += 1
    
            except Exception as e:
                # pause when twitter blocks further scraping
                if "Cannot find twitter account with name" in str(e):
                    check += 1
                    print (e,"Moving next")
                    searched=False
                else:
                    print(e, "Sleeping for 7 mins")
                    print("Check: ", check)
                    time.sleep(420)
    
        # before iterating to the next day, remove the resume file
        if searched:
            os.remove(resume_file)

    
        # increment the start date by one day
        start_date = start_date + relativedelta(days=1)
                
        repliesdf = twint.storage.panda.Tweets_df
        #test = replies[replies['conversation_id']==row['id']]
        if searched:
            if len(repliesdf)>0:
                frames = [shamereplies, repliesdf[repliesdf['conversation_id']==row['id']]]
                shamereplies = pandas.concat(frames)



######later

for index, row in df.iterrows():
    start_str = (datetime.datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S")+ relativedelta(weeks=1)).strftime("%Y-%m-%d")
    end_str = (datetime.datetime.strptime(row["date"], "%Y-%m-%d %H:%M:%S")+ relativedelta(weeks=2)).strftime("%Y-%m-%d")
    start_date = pandas.to_datetime(start_str, format='%Y-%m-%d', errors='ignore')
    end_date = pandas.to_datetime(end_str, format='%Y-%m-%d', errors='ignore')
    data_folder = "D:/Users/amita/Desktop/social psychology/thesis/code/data/"
    resume_file = r"{data_folder}resume.txt"
    replies = twint.Config()
    replies.Search = "-filter:retweets -filter:replies"
    replies.Username = row['username']
    replies.Resume = resume_file
    replies.Pandas = True
    
    while start_date < end_date:
     
        check = 0
        replies.Since = datetime.datetime.strftime(start_date, format='%Y-%m-%d')
        replies.Until = datetime.datetime.strftime(start_date + relativedelta(days=1), format='%Y-%m-%d')
    
        while check < 1:
            try:
                print("Running Search: Check ", start_date)
                twint.run.Search(replies)
                searched=True
                check += 1
    
            except Exception as e:
                # pause when twitter blocks further scraping
                if "Cannot find twitter account with name" in str(e):
                    check += 1
                    print (e,"Moving next")
                    searched=False
                else:
                    print(e, "Sleeping for 7 mins")
                    print("Check: ", check)
                    time.sleep(420)
    
        # before iterating to the next day, remove the resume file
        if searched:
            os.remove(resume_file)

    
        # increment the start date by one day
        start_date = start_date + relativedelta(days=1)
                
        repliesdf = twint.storage.panda.Tweets_df
        #test = replies[replies['conversation_id']==row['id']]
        if searched:
            if len(repliesdf)>0:
                frames = [later, repliesdf]
                later = pandas.concat(frames)
            