library(ggplot2)

summaryData = read.csv(file="data/summary_stats.csv", header = TRUE)
print(summaryData)

ggplot(summaryData, aes(x = Sport.Gender, y = Percentage, fill = Coach.Gender)) + 
  geom_bar(position = "fill", stat="identity") +
  geom_text(aes(label=paste0(Percentage,"%"))) +
  labs(x = "Sport Gender", title = "Comparing NCAA Men's and Women's Division I Sports by Coach's Gender", fill = "Coach Gender") +
  scale_y_continuous(labels = scales::percent_format())

