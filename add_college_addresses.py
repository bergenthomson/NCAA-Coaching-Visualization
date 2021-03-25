import pandas as pd

coaches = pd.read_csv("data/coaches_cleaned.csv")
locations = pd.read_csv("data/college_addresses.csv")

merged = coaches.merge(locations, on="School", how="left", sort="True")

merged.to_csv("data/coaches_with_school_addresses.csv")
