library(dplyr)
aggregated <- aggregate(.~conversation_id+`tweet(tweet)`+`username(tweet)`+emotion,data = organized,FUN = paste, collapse = " / ")
duplicated <- which(duplicated(aggregated$conversation_id)|duplicated(aggregated$conversation_id,fromLast = TRUE))
aggregated <- aggregated[-duplicated,]


lateraggregated <- select(cleanlater,username,tweet)
lateraggregated <- aggregate(.~username,data = lateraggregated,FUN = paste, collapse = " / ")

lateraggregated <- rename(lateraggregated,`tweet(later)`=tweet)
lateraggregated <- rename(lateraggregated,`username(tweet)`=username)
aggregated <- left_join(aggregated,lateraggregated,by="username(tweet)")

