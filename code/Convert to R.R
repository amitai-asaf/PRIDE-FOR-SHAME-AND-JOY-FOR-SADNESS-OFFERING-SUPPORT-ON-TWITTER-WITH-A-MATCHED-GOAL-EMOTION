library(tidyverse)

sadnessreplies1 <- read_rds("sadnessreplies1.RDS")
sadnessreplies2 <- read_rds("sadnessreplies2.RDS")
sadnessreplies3 <- read_rds("sadnessreplies3.RDS")
sadnessreplies4 <- read_rds("sadnessreplies4.RDS")

sadnessreplies <- bind_rows(sadnessreplies1,sadnessreplies2,sadnessreplies3,sadnessreplies4)


sadness <- read_rds("sadness.RDS")
shame <- read_rds("shame.RDS")
shamereplies <- read_rds("shamereplies.RDS")
extrashamereplies <- read_rds("extrashamereplies.RDS")
bind_rows(shamereplies,extrashamereplies)

