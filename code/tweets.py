# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:54:57 2020

@author: amita
"""

import twint
import nest_asyncio
import pandas
import pyreadr


##i am feeling sad

nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i am feeling sad.Rds", df)


##i am feeling sadness

nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i am feeling sadness.Rds", df)

##i am feeling shame


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i am feeling shame.Rds", df)

##i am feeling ashamed
nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am feeling ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i am feeling ashamed.Rds", df)

##i am experiencing sadness
nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am experiencing sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am experiencing sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am experiencing sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i am experiencing sadness.Rds", df)

##i am experiencing shame
nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am experiencing shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am experiencing shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am experiencing shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i am experiencing shame.Rds", df)

##i am sad
nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2019-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df

nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2029-11-20"
engine.Since = "2018-11-20"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)

nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2018-11-20"
engine.Since = "2017-11-20"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)

nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2017-11-20"
engine.Since = "2016-11-20"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)

nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2016-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
df = pandas.concat(frames)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)

nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i am sad.Rds", df)

##i am ashamed 
nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i am ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i am ashamed.Rds", df)


##i have been feeling sad


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i have been feeling sad.Rds", df)


##i have been feeling sadness


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i have been feeling sadness.Rds", df)


##i have been feeling shame


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i have been feeling shame.Rds", df)


##i have been feeling ashamed


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been feeling ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i have been feeling ashamed.Rds", df)


##i have been experiencing sadness


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been experiencing sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been experiencing sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been experiencing sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i have been experiencing sadness.Rds", df)


##i have been experiencing shame




nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been experiencing shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been experiencing shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been experiencing shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i have been experiencing shame.Rds", df)


##i have been sad
##i have been experiencing shame <#$#$#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
##i have been experiencing shame <#$#$#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
##i have been experiencing shame <#$#$#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
##i have been experiencing shame <#$#$#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
##i have been experiencing shame <#$#$#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
##i have been experiencing shame <#$#$#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
##i have been experiencing shame <#$#$#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
##i have been experiencing shame <#$#$#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
##i have been experiencing shame <#$#$#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i have been sad.Rds", df)


##i have been ashamed


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i have been ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i have been ashamed.Rds", df)


##i feel sad


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i feel sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df

nest_asyncio.apply()

nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i feel sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)

nest_asyncio.apply()

nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i feel sad\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

nest_asyncio.apply()

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i feel sad.Rds", df)


##i feel ashamed


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i feel ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i feel ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i feel ashamed\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i feel ashamed.Rds", df)


##i experience sadness


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i experience sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i experience sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i experience sadness\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i experience sadness.Rds", df)


##i experience shame


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i experience shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2020-11-20"
engine.Since = "2015-11-20"

engine.Lang ="en"
twint.run.Search(engine)
df = twint.storage.panda.Tweets_df


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i experience shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2015-11-19"
engine.Since = "2010-11-19"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)


nest_asyncio.apply()
engine=twint.Config() #create search object
engine.Search = "\"i experience shame\" -filter:retweets -filter:replies min_replies:1"
engine.Limit = 50000
engine.Pandas = True
engine.Until = "2010-11-18"
engine.Since = "2007-07-11"

engine.Lang ="en"
twint.run.Search(engine)

frames = [df, twint.storage.panda.Tweets_df]
df = pandas.concat(frames)
if(len(df)>0):
    df[["id", "conversation_id"]] = df[["conversation_id", "conversation_id"]].astype(str) 
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\pythonreplies\i experience shame.Rds", df)
