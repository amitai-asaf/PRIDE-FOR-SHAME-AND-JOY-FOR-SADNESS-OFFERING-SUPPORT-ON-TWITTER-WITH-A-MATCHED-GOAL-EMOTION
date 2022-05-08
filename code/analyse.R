library(tidyverse)
library(ggpubr)
library(normalr)
library(MASS)
library(ggplot2)
library(pscl)
library(boot)
library(glmmADMB)
library(MGLM)
library(rsq)
library(reghelper)
library(caret)
library(QuantPsyc)


#normality
shapiro.test(sample(prepsadness$`joy(reply)`,5000))
shapiro.test(sample(prepsadness$`pride(reply)`,5000))
shapiro.test(sample(prepshame$`joy(reply)`,5000))
shapiro.test(sample(prepshame$`pride(reply)`,5000))
shapiro.test(sample(sample$pride_reply,5000))
shapiro.test(sample(sample$joy_reply,5000))
shapiro.test(sample(sample$sadness_later,5000))
shapiro.test(sample(sample$shame_later,5000))

ggdensity(prepsadness$`joy(reply)`, 
          main = "Density plot of joy word count in sadness",
          xlab = "joy word count")

ggdensity(prepsadness$`pride(reply)`, 
          main = "Density plot of pride word count in sadness",
          xlab = "pride word count")

ggdensity(prepshame$`joy(reply)`, 
          main = "Density plot of joy word count in shame",
          xlab = "joy word count")

ggdensity(prepsadness$`pride(reply)`, 
          main = "Density plot of pride word count in shame",
          xlab = "pride word count")

ggdensity(prepsadness$`joy(reply)`, 
          main = "Density plot of joy word count",
          xlab = "joy word count")

ggdensity(prepsadness$`pride(reply)`, 
          main = "Density plot of pride",
          xlab = "pride word count")

####################################################### sadness

sadnesstest <- data.frame(count=c(samplesadness$`joy(reply)`, samplesadness$`pride(reply)`), emotion=factor(rep(c("joy", "pride"), c(length(samplesadness$`joy(reply)`), length(samplesadness$`pride(reply)`)))))

glmFitP <- glm(count ~ emotion, family=poisson(link="log"), data=sadnesstest)
summary(glmFitP) 


glmFitNB <- glm.nb(count ~ emotion, data=sadnesstest)
summary(glmFitNB) 

zinb<-zeroinfl(count ~ emotion, data=sadnesstest,dist = "negbin")
summary(zinb) 


#graph
predictedsadness <- data.frame(emotion=c("joy","pride"))
predictedsadness <- cbind(predictedsadness,predict(glmFitNB,predictedsadness,type="link",se.fit=TRUE))
predictedsadness <- within(predictedsadness, {
  count <- exp(fit)
  LL <- exp(fit - 1.96 * se.fit)
  UL <- exp(fit + 1.96 * se.fit)
})

ggplot(predictedsadness, aes(emotion, count)) +
  geom_bar(stat="identity", position=position_dodge())+
  geom_errorbar(aes(ymin=LL, ymax=UL), width=.2, position=position_dodge(.9))+
  labs(title="emotion response to sadness:word count", x = "Emotion", y = "exp(word count)")+
  ylim(0,1.5)

####################################################### shame
shametest <- data.frame(count=c(sampleshame$`joy(reply)`, sampleshame$`pride(reply)`), emotion=factor(rep(c("joy", "pride"), c(length(sampleshame$`joy(reply)`), length(sampleshame$`pride(reply)`)))))

glmFitP <- glm(count ~ emotion, family=poisson(link="log"), data=shametest)
summary(glmFitP) 


glmFitNB <- glm.nb(count ~ emotion, data=shametest)
summary(glmFitNB) 

zinb<-zeroinfl(count ~ emotion, data=shametest,dist = "negbin")
summary(zinb) 


#graph
predictedshame <- data.frame(emotion=c("joy","pride"))
predictedshame <- cbind(predictedshame,predict(glmFitNB,predictedshame,type="link",se.fit=TRUE))
predictedshame <- within(predictedshame, {
  count <- exp(fit)
  LL <- exp(fit - 1.96 * se.fit)
  UL <- exp(fit + 1.96 * se.fit)
})

ggplot(predictedshame, aes(emotion, count)) +
  geom_bar(stat="identity", position=position_dodge())+
  geom_errorbar(aes(ymin=LL, ymax=UL), width=.2, position=position_dodge(.9))+
  labs(title="emotion response to shame:word count", x = "Emotion", y = "exp(word count)")+
  ylim(0,1.5)

################################################joined
dvnames <- c("joy","pride")
ivnames <- "emotion"

#poisson
pmodels <- list()
for (y in dvnames){
  form <- formula(paste(y, "~", ivnames))
  pmodels[[y]] <- glm(form, data=sample, family='poisson') 
}

lapply(pmodels, summary)

#negative binomial
NBmodels <- list()

for (y in dvnames){
  form <- formula(paste(y, "~", ivnames))
  NBmodels[[y]] <- glmmadmb(form, data=sample,family="nbinom") 
}

lapply(NBmodels, summary)

#zero inflated negative binomial
zinbmodels <- list()

for (y in dvnames){
  form <- formula(paste(y, "~", ivnames))
  zinbmodels[[y]] <- zeroinfl(form, data=sample,dist = "negbin") 
}

lapply(zinbmodels, summary)

#multivariate negative multinomial
mglmodel <- MGLMreg(formula=cbind(joy,pride)~emotion+word_count,data=sample,dist="NegMN")
mglmodel

#joy model simple effect
joymodel <- glm.nb(joy ~ emotion, data=sample)
summary(joymodel) 

#pride model simple effect
pridemodel <- glm.nb(pride ~ emotion, data=sample)
summary(pridemodel)

#########################graph

predictedjoy <- data.frame(emotion=c("sadness","shame"))
predictedjoy <- cbind(predictedjoy,predict(joymodel,predictedjoy,type="link",se.fit=TRUE))
predictedjoy <- within(predictedjoy, {
  count <- exp(fit)
  LL <- exp(fit - 1.96 * se.fit)
  UL <- exp(fit + 1.96 * se.fit)
})

ggplot(predictedjoy, aes(emotion, count)) +
  geom_bar(stat="identity", position=position_dodge())+
  geom_errorbar(aes(ymin=LL, ymax=UL), width=.2, position=position_dodge(.9))+
  labs(title="emotion response to sadness:word count", x = "Emotion", y = "exp(word count)")+
  ylim(0,1.5)

############joined opposite (this is the analysis)
#reply
sample_reply <- dplyr::select(sample,conversation_id,emotion,joy_reply,pride_reply)
sample_reply <- pivot_longer(sample_reply,cols=joy_reply:pride_reply,names_to = "reply_emotion",values_to = "emotion_score")

shapiro.test(sample(sample_reply$emotion_score,5000))

ggplot(filter(sample_reply,emotion_score>0&emotion_score<=1), aes(emotion_score, fill = reply_emotion)) + 
  geom_histogram(binwidth = 0.05) + 
  facet_grid(reply_emotion ~ ., margins = TRUE, scales = "free") +
  scale_fill_discrete(name="Reply Emotion",
                      labels=c("Joy","Pride","Both")) +
  xlab("Emotion Score") + ylab("Density")


replynbmod <- glm.nb(emotion_score ~ reply_emotion*emotion, data = sample_reply)
summary(replynbmod)
rsq.partial(replynbmod,type="kl")

nullmod <- glm.nb(emotion_score ~ 1, data = sample_reply)
summary(nullmod)

anova(replynbmod,nullmod)

simple_slopes(replynbmod)



est <- cbind(Estimate = coef(replynbmod), confint(replynbmod))
exp(est)

#predicted
newdata <- data.frame(emotion=c("sadness","sadness","shame","shame"),reply_emotion=c("joy_reply","pride_reply","joy_reply","pride_reply"))
newdata <- cbind(newdata, predict(replynbmod, newdata, type = "link", se.fit=TRUE))
newdata <- within(newdata, {
  emotion_score <- exp(fit)
  LL <- exp(fit - 1.96 * se.fit)
  UL <- exp(fit + 1.96 * se.fit)
})

#ggplot(newdata, aes(reply_emotion, emotion_score)) +
#  (aes(ymin = LL, ymax = UL, fill = emotion), alpha = .25) +
#  geom_line(aes(colour = emotion), size = 2) +
#  labs(x = "Math Score", y = "Predicted Days Absent")+

ggplot(newdata, aes(emotion, emotion_score, fill=reply_emotion))+
geom_bar(stat="identity", color="black", 
         position=position_dodge()) +
  geom_errorbar(aes(ymin=LL, ymax=UL), width=.2,
                position=position_dodge(.9))

ggplot(newdata, aes(reply_emotion, emotion_score, fill=emotion))+
  geom_bar(stat="identity", color="black", 
           position=position_dodge()) +
  geom_errorbar(aes(ymin=LL, ymax=UL), width=.2,
                position=position_dodge(.9)) + 
                xlab("Reply Emotion") + ylab("Emotion Score")

#tweet
sample_tweet <- dplyr::select(sample,conversation_id,emotion,joy_tweet,pride_tweet)
sample_tweet <- pivot_longer(sample_tweet,cols=joy_tweet:pride_tweet,names_to = "tweet_emotion",values_to = "emotion_score")

ggplot(filter(sample_tweet,emotion_score>0&emotion_score<=1), aes(emotion_score, fill = tweet_emotion)) + 
  geom_histogram(binwidth = 0.05) + 
  facet_grid(tweet_emotion ~ ., margins = TRUE, scales = "free")+
  scale_fill_discrete(name="Reply Emotion",
                      labels=c("Joy","Pride","Both")) +
  xlab("Emotion Score") + ylab("Density")

tweetnbmod <- glm.nb(emotion_score ~ tweet_emotion*emotion, data = sample_tweet)
summary(tweetnbmod)
rsq.partial(tweetnbmod,type = "kl")

nullmod <- glm.nb(emotion_score ~ 1, data = sample_reply)
summary(nullmod)

anova(tweetnbmod,nullmod)

simple_slopes(tweetnbmod)

est <- cbind(Estimate = coef(tweetnbmod), confint(tweetnbmod))
exp(est)

#predicted
newdata <- data.frame(emotion=c("sadness","sadness","shame","shame"),tweet_emotion=c("joy_tweet","pride_tweet","joy_tweet","pride_tweet"))
newdata <- cbind(newdata, predict(tweetnbmod, newdata, type = "link", se.fit=TRUE))
newdata <- within(newdata, {
  emotion_score <- exp(fit)
  LL <- exp(fit - 1.96 * se.fit)
  UL <- exp(fit + 1.96 * se.fit)
})

#ggplot(newdata, aes(tweet_emotion, emotion_score)) +
#  (aes(ymin = LL, ymax = UL, fill = emotion), alpha = .25) +
#  geom_line(aes(colour = emotion), size = 2) +
#  labs(x = "Math Score", y = "Predicted Days Absent")+

ggplot(newdata, aes(emotion, emotion_score, fill=tweet_emotion))+
  geom_bar(stat="identity", color="black", 
           position=position_dodge()) +
  geom_errorbar(aes(ymin=LL, ymax=UL), width=.2,
                position=position_dodge(.9))

ggplot(newdata, aes(tweet_emotion, emotion_score, fill=emotion))+
  geom_bar(stat="identity", color="black", 
           position=position_dodge()) +
  geom_errorbar(aes(ymin=LL, ymax=UL), width=.2,
                position=position_dodge(.9)) + 
  xlab("Original Tweet Positive Emotion") + ylab("Emotion Score")

#later
sample_later <- filter(sample,!is.na(sample$`tweet(later)`))
sample_later <- dplyr::select(sample_later,conversation_id,emotion,joy_reply,pride_reply,sadness_later,shame_later,sadness_difference,shame_difference)
#sample_later <- pivot_longer(sample_later,cols=joy_reply:pride_reply,names_to = "reply_emotion",values_to = "e_count")

ggplot(sample_later, aes(sadness_difference)) + 
  geom_histogram()

ggplot(sample_later, aes(shame_difference)) + 
  geom_histogram()

lmodel <- lm(cbind(shame_difference,sadness_difference) ~ scale(joy_reply)+scale(pride_reply), data = sample_later)
summary(lmodel)

testnbmod <- glm.nb(sadness_later ~ joy_reply, data = sample)
summary(testnbmod)
rsq.partial(testnbmod,type = "kl")

sample_later_shame <- mutate(sample_later_shame,shame_difference_z=as.numeric(scale(shame_difference)))
shamemod<- lm(shame_difference ~ reply_emotion*e_count, data = sample_later)
summary(shamemod)

sadnesslaternbmod <- glm.nb(sadness_later ~ reply_emotion*e_count, data = sample)
summary(sadnesslaternbmod)
rsq.partial(sadnesslaternbmod,type = "kl")

shamelaternbmod <- glm.nb(shame_difference ~ reply_emotion*e_count, data = sample_later_shame)
summary(shamelaternbmod)
rsq.partial(shamelaternbmod,type = "kl")

est <- cbind(Estimate = coef(sadnesslaternbmod), confint(sadnesslaternbmod))
exp(est)

#predicted
newdata <- data.frame(emotion=c("sadness","sadness","shame","shame"),tweet_emotion=c("joy_tweet","pride_tweet","joy_tweet","pride_tweet"))
newdata <- cbind(newdata, predict(tweetnbmod, newdata, type = "link", se.fit=TRUE))
newdata <- within(newdata, {
  e_count <- exp(fit)
  LL <- exp(fit - 1.96 * se.fit)
  UL <- exp(fit + 1.96 * se.fit)
})

#ggplot(newdata, aes(tweet_emotion, e_count)) +
#  (aes(ymin = LL, ymax = UL, fill = emotion), alpha = .25) +
#  geom_line(aes(colour = emotion), size = 2) +
#  labs(x = "Math Score", y = "Predicted Days Absent")+

ggplot(newdata, aes(emotion, e_count, fill=tweet_emotion))+
  geom_bar(stat="identity", color="black", 
           position=position_dodge()) +
  geom_errorbar(aes(ymin=LL, ymax=UL), width=.2,
                position=position_dodge(.9))

ggplot(newdata, aes(tweet_emotion, e_count, fill=emotion))+
  geom_bar(stat="identity", color="black", 
           position=position_dodge()) +
  geom_errorbar(aes(ymin=LL, ymax=UL), width=.2,
                position=position_dodge(.9))




































































































sample <- pivot_longer(sample,cols=sadness:shame,names_to = "reply_emotion",values_to = "e_count")
sample <- filter(sample,word_count!=0)

glmFitNB <- glm.nb(e_count ~ emotion*reply_emotion+word_count, data=sample)
summary(glmFitNB) 

zinb<-zeroinfl(e_count ~ emotion*reply_emotion+word_count, data=sample,dist = "negbin")
summary(zinb) 

#CI

resp <- predict(zinb)

stat <- function(df, inds) {
  model <- formula(e_count ~ emotion*reply_emotion+word_count)
  predict(
    zeroinfl(model, dist = "negbin", link = "logit", data = df[inds, ]),
    newdata = df)
}

set.seed(2018)
res <- boot(sample, stat, R = 100)

CI <- setNames(as.data.frame(t(sapply(1:nrow(sample), function(row)
  boot.ci(res, conf = 0.95, type = "basic", index = row)$basic[, 4:5]))),
  c("lower", "upper"))

broom.mixed::tidy(zinb, effects="fixed", conf.int=TRUE)

#######################################plot
df_all <- cbind.data.frame(sample, response = predict(zinb), CI)
df_all <- filter(df_all,word_count==40)
df_trimmed<- bind_rows(head(df_all,2),tail(df_all,2))
df_exp<-mutate(df_trimmed,response=exp(response),lower=exp(lower),upper=exp(lower))
 
ggplot(tail(df_exp,2), aes(reply_emotion, e_count)) +
  geom_bar(stat="identity", position=position_dodge())+
  geom_errorbar(aes(ymin=lower, ymax=upper), width=.2, position=position_dodge(.9))+
  labs(title="emotion response to sadness:word count", x = "Emotion", y = "exp(word count)")





###############from scratch
require(foreign)
require(ggplot2)
require(MASS)

summary(sample)

ggplot(sample, aes(e_count, fill = reply_emotion)) + geom_histogram(binwidth = 1) + facet_grid(reply_emotion ~ 
                                                                                     ., scales="free", margins = TRUE)
with(sample, tapply(e_count, reply_emotion, function(x) {
  sprintf("M (SD) = %1.2f (%1.2f)", mean(x), sd(x))
}))


summary(m1 <- zeroinfl(e_count ~ emotion*reply_emotion + word_count + , data = sample))
(est <- cbind(Estimate = coef(m1), confint(m1)))

exp(est)
