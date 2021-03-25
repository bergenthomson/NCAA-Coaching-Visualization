import pandas as pd

coaches = pd.read_csv("data/coaches_with_gender.csv")

coaches["Period"] = coaches["Period"].apply(lambda x: x[:-1])
coaches["School"] = coaches["School"].apply(lambda x: x[:-1])
coaches["Sport"] = coaches["Sport"].apply(lambda x: x[:-1])

coaches.to_csv("data/cleaned_coaches.csv", index=False, encoding='utf-8-sig')
