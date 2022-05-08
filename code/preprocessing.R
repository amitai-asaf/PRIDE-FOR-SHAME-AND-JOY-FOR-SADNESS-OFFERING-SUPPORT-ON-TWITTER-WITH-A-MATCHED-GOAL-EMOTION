library(tidyverse)
library(readtext)
library(stringi)
library(quanteda)
library(SnowballC)

#dictionary
mydict<-read.csv("data/dictionaries/ones to use/emotions.csv")

joy <- wordStem(mydict$joy,language ="en")
pride <- wordStem(mydict$pride,language ="en")
sadness <- wordStem(mydict$sadness,language ="en")
shame <- wordStem(mydict$shame,language ="en")

joy<-lapply(joy, paste0, "*")
pride<-lapply(pride, paste0, "*")
sadness<-lapply(sadness, paste0, "*")
shame<-lapply(shame, paste0, "*")

joy[joy=="*"]<-NULL
pride[pride=="*"]<-NULL
sadness[sadness=="*"]<-NULL
shame[shame=="*"]<-NULL

mydict <- dictionary(list(joy=joy, 
                          pride=pride,
                          sadness=sadness,
                          shame=shame)) 
#sadness
dtm <- dfm(organizedsadness$`tweet(reply)`,tolower = TRUE, stem = TRUE,remove = stopwords("english"),remove_punct=TRUE)

dict_dtm <- dfm_lookup(dtm, mydict, nomatch = "_unmatched") 
tail(dict_dtm)
dict_dtm

df_dtm <- as.data.frame(as.matrix(dict_dtm), stringsAsFactors=False)
df_dtm <- mutate(df_dtm, sum=rowSums(df_dtm))

prepsadness <- mutate(organizedsadness,`joy(reply)`=df_dtm$joy,`pride(reply)`=df_dtm$pride,`word_count(reply)`=df_dtm$sum)

trimsadness <- dplyr::select(prepsadness,conversation_id,`joy(reply)`,`pride(reply)`)
trimsadness <- aggregate(dplyr::select(prepsadness,`joy(reply)`,`pride(reply)`), by=list(trimsadness$conversation_id), FUN=sum)
samplesadness <- sample_n(trimsadness,size=50000)

#shame
dtm <- dfm(organizedshame$`tweet(reply)`,tolower = TRUE, stem = TRUE,remove = stopwords("english"),remove_punct=TRUE)

dict_dtm <- dfm_lookup(dtm, mydict, nomatch = "_unmatched") 
tail(dict_dtm)
dict_dtm

df_dtm <- as.data.frame(as.matrix(dict_dtm), stringsAsFactors=False)
df_dtm <- mutate(df_dtm, sum=rowSums(df_dtm))

prepshame <- mutate(organizedshame,`joy(reply)`=df_dtm$joy,`pride(reply)`=df_dtm$pride,`word_count(reply)`=df_dtm$sum)

trimshame <- dplyr::select(prepshame,conversation_id,`joy(reply)`,`pride(reply)`)
trimshame <- aggregate(dplyr::select(prepshame,`joy(reply)`,`pride(reply)`), by=list(trimshame$conversation_id), FUN=sum)
sampleshame <- sample_n(trimshame,size=50000)


##########joined#############

#text cleanup

#remove URLs
aggregated$`clean_tweet(tweet)` <- qdapRegex::rm_url(aggregated$`tweet(tweet)`)
aggregated$`clean_tweet(reply)` <- qdapRegex::rm_url(aggregated$`tweet(reply)`)
aggregated$`clean_tweet(later)` <- qdapRegex::rm_url(aggregated$`tweet(later)`)

#remove emoticons
aggregated$`clean_tweet(tweet)` <-  gsub("<[^>]+>","",aggregated$`clean_tweet(tweet)`)
aggregated$`clean_tweet(reply)` <-  gsub("<[^>]+>","",aggregated$`clean_tweet(reply)`)
aggregated$`clean_tweet(later)` <-  gsub("<[^>]+>","",aggregated$`clean_tweet(later)`)


#remove hash signs
aggregated$`clean_tweet(tweet)` <- str_remove_all(aggregated$`clean_tweet(tweet)`, "#")
aggregated$`clean_tweet(reply)` <- str_remove_all(aggregated$`clean_tweet(reply)`, "#")
aggregated$`clean_tweet(later)` <- str_remove_all(aggregated$`clean_tweet(later)`, "#")

#remove mentions
aggregated$`clean_tweet(tweet)` <- gsub('@\\S+', '', aggregated$`clean_tweet(tweet)`)
aggregated$`clean_tweet(reply)` <- gsub('@\\S+', '', aggregated$`clean_tweet(reply)`)
aggregated$`clean_tweet(later)` <- gsub('@\\S+', '', aggregated$`clean_tweet(later)`)

dtm_reply <- dfm(aggregated$`clean_tweet(reply)`,tolower = TRUE, stem = TRUE,remove = stopwords("english"),remove_punct=TRUE)
dtm_reply <- dfm_weight(dtm_reply,scheme = "prop")
dtm_reply <- dfm_lookup(dtm_reply, mydict, nomatch = "_unmatched") 
dtm_reply

df_dtm_reply <- as.data.frame(as.matrix(dtm_reply), stringsAsFactors=False)

dtm_tweet <- dfm(aggregated$`clean_tweet(tweet)`,tolower = TRUE, stem = TRUE,remove = stopwords("english"),remove_punct=TRUE)
dtm_tweet <- dfm_weight(dtm_tweet,scheme = "prop")
dtm_tweet <- dfm_lookup(dtm_tweet, mydict, nomatch = "_unmatched") 
dtm_tweet

df_dtm_tweet <- as.data.frame(as.matrix(dtm_tweet), stringsAsFactors=False)

dtm_later <- dfm(aggregated$`clean_tweet(later)`,tolower = TRUE, stem = TRUE,remove = stopwords("english"),remove_punct=TRUE)
dtm_later <- dfm_weight(dtm_later,scheme = "prop")
dtm_later <- dfm_lookup(dtm_later, mydict, nomatch = "_unmatched") 
dtm_later

df_dtm_later <- as.data.frame(as.matrix(dtm_later), stringsAsFactors=False)

prepared <- mutate(aggregated,`joy(reply)`=df_dtm_reply$joy,`pride(reply)`=df_dtm_reply$pride,`joy(tweet)`=df_dtm_tweet$joy,`pride(tweet)`=df_dtm_tweet$pride,`sadness(tweet)`=df_dtm_tweet$sadness,`shame(tweet)`=df_dtm_tweet$shame,`sadness(later)`=df_dtm_later$sadness,`shame(later)`=df_dtm_later$shame)

prepared <- mutate(prepared,shame_difference=prepared$`shame(tweet)`-prepared$`shame(later)`,sadness_difference=prepared$`sadness(tweet)`-prepared$`sadness(later)`)


#trim_reply <- aggregate(dplyr::select(prepared,`joy(reply)`,`pride(reply)`), by=list(conversation_id=prepared$conversation_id), FUN=sum)
#trim_tweet <- aggregate(dplyr::select(prepared,`joy(tweet)`,`pride(tweet)`), by=list(conversation_id=prepared$conversation_id), FUN=sum)
#trim_emotion <- distinct(select(prepared,conversation_id,emotion))
#trim_emotion<- filter(trim_emotion,!duplicated(trim_emotion$conversation_id))
#trim <- mutate(trim_tweet,`joy(reply)`=trim_reply$`joy(reply)`,`pride(reply)`=trim_reply$`pride(reply)`)
#trim <- merge(trim,trim_emotion,by="conversation_id")

#sample <- trim %>%
#            group_by(emotion) %>%
#              sample_n(50000) %>%
#                ungroup()

sample <- prepared %>%
            group_by(emotion) %>%
              sample_n(50000) %>%
                ungroup()


sample <- sample%>%
            rename(joy_tweet=`joy(tweet)`,pride_tweet=`pride(tweet)`,joy_reply=`joy(reply)`,pride_reply=`pride(reply)`,joy_tweet_z=`joy(tweet)_z`,pride_tweet_z=`pride(tweet)_z`,joy_reply_z=`joy(reply)_z`,pride_reply_z=`pride(reply)_z`)

sample <- mutate(sample,user=prepared$username)
####################### transfering the sampled tweets to python to get the later tweets
which(!later$conversation_id%in%aggregated$conversation_id)

later1 <- later[-which(!later$conversation_id%in%aggregated$conversation_id),]

sample <- prepared[!prepared$conversation_id%in%later1$conversation_id,]
sample <- filter(sample,sample$emotion=="sadness")

cleansadness <- filter(cleansadness,cleansadness$conversation_id%in%later2$conversation_id)

later2 <- sample_n(sample,6)
later2 <-select(cleansadness,conversation_id,username,date)
saveRDS(later1,"data/later1.Rds")
saveRDS(later2,"data/later2.Rds")
readRDS("data/later2.Rds")

################## getting the same tweets that were sampled for later tweets analysis
sample <- bind_rows(laterfromR1,laterfromR2)

sample <- filter(prepared,prepared$conversation_id%in%sample$conversation_id) %>%
            rename(joy_tweet=`joy(tweet)`,pride_tweet=`pride(tweet)`,joy_reply=`joy(reply)`,pride_reply=`pride(reply)`,sadness_tweet=`sadness(tweet)`,shame_tweet=`shame(tweet)`,sadness_later=`sadness(later)`,shame_later=`shame(later)`)