library(tidyverse)

cleanlater1 <- later1
cleanlater1 <- filter(cleanlater1,cleanlater1$language=="en")
cleanlater1 <- select(cleanlater1,conversation_id,username,date,tweet)
#filter(cleanlater1,date >= as.Date("2014-01-05"))

cleanlater2 <- later2
cleanlater2 <- filter(cleanlater2,cleanlater2$language=="en")
cleanlater2 <- select(cleanlater2,conversation_id,username,date,tweet)

cleanlater3 <- later3
cleanlater3 <- filter(cleanlater3,cleanlater3$language=="en")
cleanlater3 <- select(cleanlater3,conversation_id,username,date,tweet)

cleanlater4 <- later4
cleanlater4 <- filter(cleanlater4,cleanlater4$language=="en")
cleanlater4 <- select(cleanlater4,conversation_id,username,date,tweet)

cleanlater5 <- later5
cleanlater5 <- filter(cleanlater5,cleanlater5$language=="en")
cleanlater5 <- select(cleanlater5,conversation_id,username,date,tweet)

cleanlater6 <- later6
cleanlater6 <- filter(cleanlater6,cleanlater6$language=="en")
cleanlater6 <- select(cleanlater6,conversation_id,username,date,tweet)

cleanlater7 <- later7
cleanlater7 <- filter(cleanlater7,cleanlater7$language=="en")
cleanlater7 <- select(cleanlater7,conversation_id,username,date,tweet)

cleanlater8 <- later8
cleanlater8 <- filter(cleanlater8,cleanlater8$language=="en")
cleanlater8 <- select(cleanlater8,conversation_id,username,date,tweet)

cleanlater9 <- later9
cleanlater9 <- filter(cleanlater9,cleanlater9$language=="en")
cleanlater9 <- select(cleanlater9,conversation_id,username,date,tweet)

cleanlater10 <- later10
cleanlater10 <- filter(cleanlater10,cleanlater10$language=="en")
cleanlater10 <- select(cleanlater10,conversation_id,username,date,tweet)

cleanlater <- union(cleanlater1,cleanlater2,cleanlater3,cleanlater4,cleanlater5,cleanlater6,cleanlater7,cleanlater8,cleanlater9,cleanlater10)

test <- left_join()