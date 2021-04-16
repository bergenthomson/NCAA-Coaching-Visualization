import pandas as pd

coaches = pd.read_csv("data/coaches_with_latlng.csv")
coachGenders = coaches["gender"]
sports = coaches["Sport"]






def getCounts(sport):
    numCoachesByGender = {"man": 0, "woman": 0}
    for i in range(len(sports)):
        if sport in sports[i]:
            if coachGenders[i] == "male":
                numCoachesByGender["man"] += 1
            else:
                numCoachesByGender["woman"] += 1
    return numCoachesByGender
