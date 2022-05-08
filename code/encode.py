# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 13:52:01 2021

@author: amita
"""
import pandas
import pyreadr





#sample
df['a'] = df['a'].apply(lambda x: x + 1)
x.encode('utf-8')
x.decode('utf-8')

#reset index
sadnessreplies1=sadnessreplies1.reset_index(drop=True)
sadnessreplies2=sadnessreplies2.reset_index(drop=True)
sadnessreplies3=sadnessreplies3.reset_index(drop=True)
sadnessreplies4=sadnessreplies4.reset_index(drop=True)
shamereplies=shamereplies.reset_index(drop=True)
shame=shame.reset_index(drop=True)
sadness=sadness.reset_index(drop=True)
extrashamereplies=shamelater.reset_index(drop=True)

later1=later1.reset_index(drop=True)
later2=later2.reset_index(drop=True)
later3=later3.reset_index(drop=True)
later4=later4.reset_index(drop=True)
later5=later5.reset_index(drop=True)
later6=later6.reset_index(drop=True)
later7=later7.reset_index(drop=True)
later8=later8.reset_index(drop=True)
later9=later9.reset_index(drop=True)
later10=later10.reset_index(drop=True)



#sadnessreplies
for i in range(len(sadnessreplies1)) : 
  sadnessreplies1.loc[i, "name"]=str(sadnessreplies1.loc[i, "name"].encode('utf-8'))[2:-1]
  sadnessreplies1.loc[i, "tweet"]=str(sadnessreplies1.loc[i, "tweet"].encode('utf-8'))[2:-1]
  sadnessreplies1.loc[i, "username"]=str(sadnessreplies1.loc[i, "username"].encode('utf-8'))[2:-1]
  
for i in range(len(sadnessreplies2)) : 
  sadnessreplies2.loc[i, "name"]=str(sadnessreplies2.loc[i, "name"].encode('utf-8'))[2:-1]
  sadnessreplies2.loc[i, "tweet"]=str(sadnessreplies2.loc[i, "tweet"].encode('utf-8'))[2:-1]
  sadnessreplies2.loc[i, "username"]=str(sadnessreplies2.loc[i, "username"].encode('utf-8'))[2:-1]
  
for i in range(len(sadnessreplies3)) : 
  sadnessreplies3.loc[i, "name"]=str(sadnessreplies3.loc[i, "name"].encode('utf-8'))[2:-1]
  sadnessreplies3.loc[i, "tweet"]=str(sadnessreplies3.loc[i, "tweet"].encode('utf-8'))[2:-1]
  sadnessreplies3.loc[i, "username"]=str(sadnessreplies3.loc[i, "username"].encode('utf-8'))[2:-1]
  
for i in range(len(sadnessreplies4)) : 
  sadnessreplies4.loc[i, "name"]=str(sadnessreplies4.loc[i, "name"].encode('utf-8'))[2:-1]
  sadnessreplies4.loc[i, "tweet"]=str(sadnessreplies4.loc[i, "tweet"].encode('utf-8'))[2:-1]
  sadnessreplies4.loc[i, "username"]=str(sadnessreplies4.loc[i, "username"].encode('utf-8'))[2:-1]
  
#shame replies
for i in range(len(shamereplies)) : 
  shamereplies.loc[i, "name"]=str(shamereplies.loc[i, "name"].encode('utf-8'))[2:-1]
  shamereplies.loc[i, "tweet"]=str(shamereplies.loc[i, "tweet"].encode('utf-8'))[2:-1]
  shamereplies.loc[i, "username"]=str(shamereplies.loc[i, "username"].encode('utf-8'))[2:-1]

#sadness
for i in range(len(sadness)) : 
  sadness.loc[i, "name"]=str(sadness.loc[i, "name"].encode('utf-8'))[2:-1]
  sadness.loc[i, "tweet"]=str(sadness.loc[i, "tweet"].encode('utf-8'))[2:-1]
  sadness.loc[i, "username"]=str(sadness.loc[i, "username"].encode('utf-8'))[2:-1]

#shame

for i in range(len(shame)) : 
  shame.loc[i, "name"]=str(shame.loc[i, "name"].encode('utf-8'))[2:-1]
  shame.loc[i, "tweet"]=str(shame.loc[i, "tweet"].encode('utf-8'))[2:-1]
  shame.loc[i, "username"]=str(shame.loc[i, "username"].encode('utf-8'))[2:-1]

for i in range(len(extrashamereplies)) : 
  extrashamereplies.loc[i, "name"]=str(extrashamereplies.loc[i, "name"].encode('utf-8'))[2:-1]
  extrashamereplies.loc[i, "tweet"]=str(extrashamereplies.loc[i, "tweet"].encode('utf-8'))[2:-1]
  extrashamereplies.loc[i, "username"]=str(extrashamereplies.loc[i, "username"].encode('utf-8'))[2:-1]



for i in range(838987,len(later1)) : 
  later1.loc[i, "name"]=str(later1.loc[i, "name"].encode('utf-8'))[2:-1]
  later1.loc[i, "tweet"]=str(later1.loc[i, "tweet"].encode('utf-8'))[2:-1]
  later1.loc[i, "username"]=str(later1.loc[i, "username"].encode('utf-8'))[2:-1]
  print(i)

for i in range(len(later2)) : 
  later2.loc[i, "name"]=str(later2.loc[i, "name"].encode('utf-8'))[2:-1]
  later2.loc[i, "tweet"]=str(later2.loc[i, "tweet"].encode('utf-8'))[2:-1]
  later2.loc[i, "username"]=str(later2.loc[i, "username"].encode('utf-8'))[2:-1]
  print(i)

pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later2.Rds", later2)
del later2

for i in range(len(later3)) : 
  later3.loc[i, "name"]=str(later3.loc[i, "name"].encode('utf-8'))[2:-1]
  later3.loc[i, "tweet"]=str(later3.loc[i, "tweet"].encode('utf-8'))[2:-1]
  later3.loc[i, "username"]=str(later3.loc[i, "username"].encode('utf-8'))[2:-1]
  print(3,i)

pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later3.Rds", later3)
del later3

for i in range(len(later4)) : 
  later4.loc[i, "name"]=str(later4.loc[i, "name"].encode('utf-8'))[2:-1]
  later4.loc[i, "tweet"]=str(later4.loc[i, "tweet"].encode('utf-8'))[2:-1]
  later4.loc[i, "username"]=str(later4.loc[i, "username"].encode('utf-8'))[2:-1]
  print(4,i)

pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later4.Rds", later4)
del later4

for i in range(len(later5)) : 
  later5.loc[i, "name"]=str(later5.loc[i, "name"].encode('utf-8'))[2:-1]
  later5.loc[i, "tweet"]=str(later5.loc[i, "tweet"].encode('utf-8'))[2:-1]
  later5.loc[i, "username"]=str(later5.loc[i, "username"].encode('utf-8'))[2:-1]
  print(5,i)

pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later5.Rds", later5)
del later5

for i in range(len(later6)) : 
  later6.loc[i, "name"]=str(later6.loc[i, "name"].encode('utf-8'))[2:-1]
  later6.loc[i, "tweet"]=str(later6.loc[i, "tweet"].encode('utf-8'))[2:-1]
  later6.loc[i, "username"]=str(later6.loc[i, "username"].encode('utf-8'))[2:-1]
  print(i)

for i in range(len(later7)) : 
  later7.loc[i, "name"]=str(later7.loc[i, "name"].encode('utf-8'))[2:-1]
  later7.loc[i, "tweet"]=str(later7.loc[i, "tweet"].encode('utf-8'))[2:-1]
  later7.loc[i, "username"]=str(later7.loc[i, "username"].encode('utf-8'))[2:-1]
  print(i)
  
for i in range(len(later8)) : 
  later8.loc[i, "name"]=str(later8.loc[i, "name"].encode('utf-8'))[2:-1]
  later8.loc[i, "tweet"]=str(later8.loc[i, "tweet"].encode('utf-8'))[2:-1]
  later8.loc[i, "username"]=str(later8.loc[i, "username"].encode('utf-8'))[2:-1]
  print(i)
  
for i in range(len(later9)) : 
  later9.loc[i, "name"]=str(later9.loc[i, "name"].encode('utf-8'))[2:-1]
  later9.loc[i, "tweet"]=str(later9.loc[i, "tweet"].encode('utf-8'))[2:-1]
  later9.loc[i, "username"]=str(later9.loc[i, "username"].encode('utf-8'))[2:-1]
  print(i)
  
for i in range(len(later10)) : 
  later10.loc[i, "name"]=str(later10.loc[i, "name"].encode('utf-8'))[2:-1]
  later10.loc[i, "tweet"]=str(later10.loc[i, "tweet"].encode('utf-8'))[2:-1]
  later10.loc[i, "username"]=str(later10.loc[i, "username"].encode('utf-8'))[2:-1]
  print(i)
  
#write to rds

pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\sadness.Rds", sadness)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\sadnessreplies1.Rds", sadnessreplies1)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\sadnessreplies2.Rds", sadnessreplies2)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\sadnessreplies3.Rds", sadnessreplies3)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\sadnessreplies4.Rds", sadnessreplies4)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\shame.Rds", shame)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\shamereplies.Rds", shamereplies)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\extrashamereplies.Rds", extrashamereplies)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later1.Rds", later1)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later2.Rds", later2)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later3.Rds", later3)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later4.Rds", later4)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later5.Rds", later5)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later6.Rds", later6)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later7.Rds", later7)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later8.Rds", later8)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later9.Rds", later9)
pyreadr.write_rds(r"D:\Users\amita\Desktop\social psychology\thesis\code\data\later10.Rds", later10)