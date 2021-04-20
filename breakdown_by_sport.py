import pandas as pd
from collections import OrderedDict

coaches = pd.read_csv("data/coaches_with_latlng.csv")
coachGenders = coaches["gender"]
sports = coaches["Sport"]


def getCoachGenderCounts(sport):
    numCoachesByGender = {"man": 0, "woman": 0}
    for i in range(len(sports)):
        if sport in sports[i]:
            if coachGenders[i] == "male":
                numCoachesByGender["man"] += 1
            else:
                numCoachesByGender["woman"] += 1
        if sports[i] == "Men's Basketball" and coachGenders[i] == "female":
            print(coaches["School"][i])
    return numCoachesByGender

# To keep track of all the unique sports and their counts
sportsWithTotalCount = OrderedDict()
for i in range(len(sports)):
    if sports[i] not in sportsWithTotalCount:
        sportsWithTotalCount[sports[i]] = 1
    else:
        sportsWithTotalCount[sports[i]] += 1

# Get counts of coach genders in each sport
sportsWithCoachGenderCounts = OrderedDict()
sportsWithMenCoachCounts = OrderedDict()
sportsWithWomenCoachCounts = OrderedDict()
# Percentage of each gender coaching each sport
sportsWithCoachGenderPercentage = OrderedDict()
sportsWithMenCoachPercentage = OrderedDict()
sportsWithWomenCoachPercentage = OrderedDict()
for s in sportsWithTotalCount.keys():
    sportsWithCoachGenderCounts[s] = getCoachGenderCounts(s)
    sportsWithMenCoachCounts[s] = sportsWithCoachGenderCounts[s]["man"]
    sportsWithWomenCoachCounts[s] = sportsWithCoachGenderCounts[s]["woman"]
    sportsWithCoachGenderPercentage[s] = {"man": round((sportsWithCoachGenderCounts[s]["man"]/sportsWithTotalCount[s]) * 100, 2), "woman": round((sportsWithCoachGenderCounts[s]["woman"]/sportsWithTotalCount[s]) * 100, 2)}
    sportsWithMenCoachPercentage[s] = sportsWithCoachGenderPercentage[s]["man"]
    sportsWithWomenCoachPercentage[s] = sportsWithCoachGenderPercentage[s]["woman"]

df = pd.DataFrame(data = { "Sport": list(sportsWithTotalCount.keys()), "Number of Total Coaches": list(sportsWithTotalCount.values()), "Number of Men Coaches": list(sportsWithMenCoachCounts.values()), "Number of Women Coaches": list(sportsWithWomenCoachCounts.values()), "Percentage Men Coaches": list(sportsWithMenCoachPercentage.values()), "Percentage Women Coaches": list(sportsWithWomenCoachPercentage.values()) })
df.to_csv("data/breakdown_by_sport.csv", index=False)
