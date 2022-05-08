library(tweetbotornot2)
library(tidyverse)

#מספרים התחלתיים
#עצב 193839
# בושה 69893
#620305 תגובות לעצב
#תגובות לבושה312214 

cleansadness <- sadness
cleanshame <- shame
cleansadnessreplies <- sadnessreplies
cleanshamereplies <- shamereplies
cleanextrashamereplies <- extrashamereplies
  
#file <- try(fread(file.name))
#if (class(file) == “try-error”)

cleansadnessreplies <- filter(cleansadnessreplies,cleansadnessreplies$language=="en")
cleanshamereplies <- filter(cleanshamereplies,cleanshamereplies$conversation_id%in%shamereplies$conversation_id)
cleanextrashamereplies <- filter(cleanextrashamereplies,cleanextrashamereplies$language=="en")

for (i in seq(3801,nrow(sadness),by=100))
{
  repeat
  {
    predicts <- try(predict_bot(as.character(na.omit(sadness$username[i:(i+99)]))))
    if (class(predicts) != "try-error")
    {
      predicts <- filter(predicts,prob_bot > 0.7)
      cleansadness <- filter(cleansadness,!use.*rname%in%predicts$screen_name)
      print("sadness")
      print(i)
      break
    }
  }
}

for (i in seq(1,nrow(shame),by=100))
{
  repeat
  {
    predicts <- try(predict_bot(as.character(na.omit(shame$username[i:(i+99)]))))
    if (class(predicts) != "try-error")
    {
      predicts <- filter(predicts,prob_bot > 0.7)
      cleanshame <- filter(cleanshame,!username%in%predicts$screen_name)
      print("shame")
      print(i)
      break
    }
  }
}

for (i in seq(115801,nrow(sadnessreplies),by=100))
{
  repeat
  {
    predicts <- try(predict_bot(as.character(na.omit(sadnessreplies$username[i:(i+99)]))))
    if (class(predicts) != "try-error")
    {
      predicts <- filter(predicts,prob_bot > 0.7)
      cleansadnessreplies <- filter(cleansadnessreplies,!username%in%predicts$screen_name)
      print("sadnessreplies")
      print(i)
      break
    }
  }
}

for (i in seq(1,nrow(shamereplies),by=100))
{
  repeat
  {
    predicts <- try(predict_bot(as.character(na.omit(shamereplies$username[i:(i+99)]))))
    if (class(predicts) != "try-error")
    {
      predicts <- filter(predicts,prob_bot > 0.7)
      cleanshamereplies <- filter(cleanshamereplies,!username%in%predicts$screen_name)
      print("shamereplies")
      print(i)
      break
    }
  }
}

for (i in seq(1,nrow(extrashamereplies),by=100))
{
  repeat
  {
    predicts <- try(predict_bot(as.character(na.omit(extrashamereplies$username[i:(i+99)]))))
    if (class(predicts) != "try-error")
    {
      predicts <- filter(predicts,prob_bot > 0.7)
      cleanextrashamereplies <- filter(cleanextrashamereplies,!username%in%predicts$screen_name)
      print("extrashamereplies")
      print(i)
      break
    }
  }
}

cleanshamereplies <- filter(cleanshamereplies,cleanshamereplies$conversation_id%in%cleanshame$conversation_id)
cleanshame <- filter(cleanshame,cleanshame$conversation_id%in%cleanshamereplies$conversation_id)
cleansadnessreplies <- filter(cleansadnessreplies,cleansadnessreplies$conversation_id%in%cleansadness$conversation_id)
cleansadness <- filter(cleansadness,cleansadness$conversation_id%in%cleansadnessreplies$conversation_id)

shamenoreplies <- filter(cleanshame,!cleanshame$conversation_id%in%cleanshamereplies$conversation_id)
saveRDS(shamenoreplies,"D:/Users/amita/Desktop/social psychology/thesis/code/data/shameretry.Rds")

cleanshamereplies <- bind_rows(cleanshamereplies,cleanextrashamereplies)
shameretry <- readRDS("D:/Users/amita/Desktop/social psychology/thesis/code/data/shameretry.Rds")
cleanshame <- bind_rows(cleanshame,shameretry)
