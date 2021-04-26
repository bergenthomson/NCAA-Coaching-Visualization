import pandas as pd
from collections import OrderedDict

coaches = pd.read_csv("data/coaches_duplicate_sports_removed.csv")
coachGenders = coaches["gender"]
schools = coaches["School"]
lats = coaches["Latitude"]
lngs = coaches["Longitude"]

schoolsWithCoachGenderCounts = OrderedDict()
schoolsWithTotalCount = OrderedDict()
schoolLngs = OrderedDict()
schoolLats = OrderedDict()
for i in range(len(schools)):
    school = schools[i]
    if school in schoolsWithCoachGenderCounts.keys():
        if coachGenders[i] == "male":
            schoolsWithCoachGenderCounts[school]["man"] += 1
        else:
            schoolsWithCoachGenderCounts[school]["woman"] += 1
        schoolsWithTotalCount[school] += 1
    else:
        if coachGenders[i] == "male":
            schoolsWithCoachGenderCounts[school] = {"man": 1, "woman": 0}
        else:
            schoolsWithCoachGenderCounts[school] = {"man": 0, "woman": 1}
        schoolsWithTotalCount[school] = 1
        schoolLngs[school] = lngs[i]
        schoolLats[school] = lats[i]

# Add breakdown of men's and women's sports at each school?


# Get counts of coach genders at each school
schoolsWithMenCoachCounts = OrderedDict()
schoolsWithWomenCoachCounts = OrderedDict()
# Percentage of each gender coaching at each school
schoolsWithCoachGenderPercentage = OrderedDict()
schoolsWithMenCoachPercentage = OrderedDict()
schoolsWithWomenCoachPercentage = OrderedDict()
for s in schoolsWithTotalCount.keys():
    schoolsWithMenCoachCounts[s] = schoolsWithCoachGenderCounts[s]["man"]
    schoolsWithWomenCoachCounts[s] = schoolsWithCoachGenderCounts[s]["woman"]
    schoolsWithCoachGenderPercentage[s] = {"man": round((schoolsWithCoachGenderCounts[s]["man"]/schoolsWithTotalCount[s]) * 100, 2), "woman": round((schoolsWithCoachGenderCounts[s]["woman"]/schoolsWithTotalCount[s]) * 100, 2)}
    schoolsWithMenCoachPercentage[s] = schoolsWithCoachGenderPercentage[s]["man"]
    schoolsWithWomenCoachPercentage[s] = schoolsWithCoachGenderPercentage[s]["woman"]

df = pd.DataFrame(data = { "School": list(schoolsWithTotalCount.keys()), "lat": list(schoolLats.values()), "lng": list(schoolLngs.values()), "Number of DI Sports": list(schoolsWithTotalCount.values()), "Number of Men Head Coaches": list(schoolsWithMenCoachCounts.values()), "Number of Women Head Coaches": list(schoolsWithWomenCoachCounts.values()), "Percentage Men Coaches": list(schoolsWithMenCoachPercentage.values()), "Percentage Women Coaches": list(schoolsWithWomenCoachPercentage.values()) })
df.to_csv("data/breakdown_by_school.csv", index=False)
