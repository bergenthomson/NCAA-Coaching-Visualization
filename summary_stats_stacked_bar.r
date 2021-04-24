library(ggplot2)
library(plyr)
library(scales)
library(tidyverse)

summaryData = read.csv(file="data/summary_stats.csv", header = TRUE)
summaryData$Percentage <- as.numeric(summaryData$Percentage)
summaryData <- ddply(summaryData, .(Sport.Gender), transform, pos = cumsum(Percentage) - (0.5*Percentage))
print(summaryData)

# ggplot(summaryData, aes(x = Sport.Gender, y = Percentage, fill = Coach.Gender)) + 
#   geom_bar(position = "fill", stat="identity") +
#   geom_text(aes(x = Sport.Gender, y = pos, label=paste0(Percentage,"%")), position = position_stack(vjust=0.1)) +
#   labs(x = "Sport Gender", title = "Comparing NCAA Men's and Women's Division I Sports by Coach's Gender", fill = "Coach Gender") +
#   scale_y_continuous(labels = scales::percent_format())


# fill <- c("#5F9EA0", "#E1B378")
# ggplot() + 
#   geom_bar(data=summaryData, aes(x=Sport.Gender, y=Percentage, fill=fct_reorder(Coach.Gender, Percentage)), stat="identity") +
#   geom_text(data=summaryData, aes(x=Sport.Gender, y=pos, label=paste0(Percentage,"%"))) +
#   labs(x = "Sport Gender", title = "Comparing NCAA Men's and Women's Division I Sports by Coach's Gender", fill = "Coach Gender") +
#   scale_y_continuous(labels = dollar_format(suffix = "%", prefix="")) +
#   scale_fill_manual(values=fill)

fill <- c("#5F9EA0", "#E1B378")
ggplot(summaryData, aes(x=Sport.Gender, y=Percentage, fill=fct_reorder(Coach.Gender, Percentage), label=paste0(Percentage,"%"))) + 
  geom_bar(stat="identity") +
  geom_text(size=4, position = position_stack(vjust = 0.5)) +
  labs(x = "Sport Gender", title = "Comparing NCAA Men's and Women's Division I Sports by Coach's Gender", fill = "Coach Gender") +
  scale_y_continuous(labels = dollar_format(suffix = "%", prefix="")) +
  scale_fill_manual(values=fill)
