library(tidyverse)

#sadness
organizedsadness <- mutate(cleansadness,emotion="sadness")
organizedsadness <- merge(organizedsadness,cleansadnessreplies,by="conversation_id",suffixes = c("(tweet)","(reply)"))
organizedsadness <- distinct(organizedsadness)



#shame
organizedshame <- mutate(cleanshame,emotion="shame")
organizedshame <- merge(organizedshame,cleanshamereplies,by="conversation_id",suffixes = c("(tweet)","(reply)"))
organizedshame <- distinct(organizedshame)

#join
organized <- bind_rows(organizedsadness,organizedshame)
organized <- select(organized,conversation_id,`tweet(tweet)`,`username(tweet)`,emotion,`id(reply)`,`tweet(reply)`,`username(reply)`)