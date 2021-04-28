import pandas as pd
from collections import OrderedDict

coaches = pd.read_csv("data/coaches_duplicate_sports_removed.csv")
coachGenders = coaches["gender"]
schools = coaches["School"]
sports = coaches["Sport"]
lats = coaches["Latitude"]
lngs = coaches["Longitude"]

schoolsWithCoachGenderCounts = OrderedDict()
schoolsWithSportGenderCoachGenderCounts = OrderedDict()
schoolsWithTotalCount = OrderedDict()
schoolsWithWomensSportsCount = OrderedDict()
schoolsWithMensSportsCount = OrderedDict()
schoolLngs = OrderedDict()
schoolLats = OrderedDict()
for i in range(len(schools)):
    school = schools[i]
    if school in schoolsWithCoachGenderCounts.keys():
        if coachGenders[i] == "male":
            schoolsWithCoachGenderCounts[school]["man"] += 1
        else:
            schoolsWithCoachGenderCounts[school]["woman"] += 1
        if "Men" in sports[i] or sports[i] in ["Football", "Baseball"]:
            schoolsWithMensSportsCount[school] += 1
            if coachGenders[i] == "male":
                schoolsWithSportGenderCoachGenderCounts[school]["mensSportManCoach"] += 1
            else:
                schoolsWithSportGenderCoachGenderCounts[school]["mensSportWomanCoach"] += 1
        if "Women" in sports[i] or sports[i] in ["Field Hockey", "Softball"]:
            schoolsWithWomensSportsCount[school] += 1
            if coachGenders[i] == "male":
                schoolsWithSportGenderCoachGenderCounts[school]["womensSportManCoach"] += 1
            else:
                schoolsWithSportGenderCoachGenderCounts[school]["womensSportWomanCoach"] += 1
        schoolsWithTotalCount[school] += 1
    else:
        if coachGenders[i] == "male":
            schoolsWithCoachGenderCounts[school] = {"man": 1, "woman": 0}
        else:
            schoolsWithCoachGenderCounts[school] = {"man": 0, "woman": 1}
        if "Men" in sports[i] or sports[i] in ["Football", "Baseball"]:
            schoolsWithMensSportsCount[school] = 1
            schoolsWithWomensSportsCount[school] = 0
            if coachGenders[i] == "male":
                schoolsWithSportGenderCoachGenderCounts[school] = {"mensSportManCoach": 1, "mensSportWomanCoach": 0, "womensSportManCoach": 0, "womensSportWomanCoach": 0}
            else:
                schoolsWithSportGenderCoachGenderCounts[school] = {"mensSportManCoach": 0, "mensSportWomanCoach": 1, "womensSportManCoach": 0, "womensSportWomanCoach": 0}
        if "Women" in sports[i] or sports[i] in ["Field Hockey", "Softball"]:
            schoolsWithWomensSportsCount[school] = 1
            schoolsWithMensSportsCount[school] = 0
            if coachGenders[i] == "male":
                schoolsWithSportGenderCoachGenderCounts[school] = {"mensSportManCoach": 0, "mensSportWomanCoach": 0, "womensSportManCoach": 1, "womensSportWomanCoach": 0}
            else:
                schoolsWithSportGenderCoachGenderCounts[school] = {"mensSportManCoach": 0, "mensSportWomanCoach": 0, "womensSportManCoach": 0, "womensSportWomanCoach": 1}
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
# Percentage of each sport gender coached by each coach gender at each school
schoolsWithWomensSportsWomanCoachPercentage = OrderedDict()
schoolsWithWomensSportsManCoachPercentage = OrderedDict()
schoolsWithMensSportsWomanCoachPercentage = OrderedDict()
schoolsWithMensSportsManCoachPercentage = OrderedDict()
for s in schoolsWithTotalCount.keys():
    schoolsWithMenCoachCounts[s] = schoolsWithCoachGenderCounts[s]["man"]
    schoolsWithWomenCoachCounts[s] = schoolsWithCoachGenderCounts[s]["woman"]
    schoolsWithCoachGenderPercentage[s] = {"man": round((schoolsWithCoachGenderCounts[s]["man"]/schoolsWithTotalCount[s]) * 100, 2), "woman": round((schoolsWithCoachGenderCounts[s]["woman"]/schoolsWithTotalCount[s]) * 100, 2)}
    schoolsWithMenCoachPercentage[s] = schoolsWithCoachGenderPercentage[s]["man"]
    schoolsWithWomenCoachPercentage[s] = schoolsWithCoachGenderPercentage[s]["woman"]

    if schoolsWithWomensSportsCount[s] != 0:
        schoolsWithWomensSportsWomanCoachPercentage[s] = round((schoolsWithSportGenderCoachGenderCounts[s]["womensSportWomanCoach"]/schoolsWithWomensSportsCount[s]) * 100, 2)
        schoolsWithWomensSportsManCoachPercentage[s] = round((schoolsWithSportGenderCoachGenderCounts[s]["womensSportManCoach"]/schoolsWithWomensSportsCount[s]) * 100, 2)
    else:
        schoolsWithWomensSportsWomanCoachPercentage[s] = 0
        schoolsWithWomensSportsManCoachPercentage[s] = 0
    if schoolsWithMensSportsCount[s] != 0:
        schoolsWithMensSportsWomanCoachPercentage[s] = round((schoolsWithSportGenderCoachGenderCounts[s]["mensSportWomanCoach"]/schoolsWithMensSportsCount[s]) * 100, 2)
        schoolsWithMensSportsManCoachPercentage[s] = round((schoolsWithSportGenderCoachGenderCounts[s]["mensSportManCoach"]/schoolsWithMensSportsCount[s]) * 100, 2)
    else:
        schoolsWithMensSportsWomanCoachPercentage[s] = 0
        schoolsWithMensSportsManCoachPercentage[s] = 0

df = pd.DataFrame(data = { "School": list(schoolsWithTotalCount.keys()), "lat": list(schoolLats.values()), "lng": list(schoolLngs.values()), "Number of DI Sports": list(schoolsWithTotalCount.values()), "Number of Men Head Coaches": list(schoolsWithMenCoachCounts.values()), "Number of Women Head Coaches": list(schoolsWithWomenCoachCounts.values()), "Percentage Men Coaches": list(schoolsWithMenCoachPercentage.values()), "Percentage Women Coaches": list(schoolsWithWomenCoachPercentage.values()), "Percentage Men's Sports Coached By Men": list(schoolsWithMensSportsManCoachPercentage.values()), "Percentage Men's Sports Coached By Women": list(schoolsWithMensSportsWomanCoachPercentage.values()), "Percentage Women's Sports Coached By Men": list(schoolsWithWomensSportsManCoachPercentage.values()), "Percentage Women's Sports Coached By Women": list(schoolsWithWomensSportsWomanCoachPercentage.values()) })
df.to_csv("data/breakdown_by_school.csv", index=False)
