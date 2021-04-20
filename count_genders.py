import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)

coaches = pd.read_csv("data/coaches_duplicate_sports_removed.csv")

coachGenders = coaches["gender"]
sports = coaches["Sport"]


coachGenderSportGender = []
numMenSports = 0
numWomenSports = 0
numTotalSports = 0
for i in range(len(coachGenders)):
    if "Men" not in sports[i] and "Women" not in sports[i] and sports[i] not in ["Mixed Rifle", "Football", "Baseball", "Field Hockey", "Softball"]:
        print(sports[i])
    if sports[i] == "Mixed Rifle":
        continue
    if "Men" in sports[i] or sports[i] in ["Football", "Baseball"]:     # Mixed rifle?
        coachGenderSportGender.append((coachGenders[i], "men"))
        numMenSports += 1
    if "Women" in sports[i] or sports[i] in ["Field Hockey", "Softball"]:
        coachGenderSportGender.append((coachGenders[i], "women"))
        numWomenSports += 1
    numTotalSports += 1

menCoaches = 0
womenCoaches = 0

menCoachingMenSports = 0
menCoachingWomenSports = 0
womenCoachingMenSports = 0
womenCoachingWomenSports = 0
for t in coachGenderSportGender:
    if t[0] == "male" and t[1] == "men":
        menCoaches += 1
        menCoachingMenSports += 1
    if t[0] == "male" and t[1] == "women":
        menCoaches += 1
        menCoachingWomenSports += 1
    if t[0] == "female" and t[1] == "men":
        womenCoaches += 1
        womenCoachingMenSports += 1
    if t[0] == "female" and t[1] == "women":
        womenCoaches += 1
        womenCoachingWomenSports += 1

print("Number of Sports Coached by Men: " + str(menCoaches))
print("Number of Sports Coached by Women: " + str(womenCoaches))

print("Number of Men's Sports Coached by Men: " + str(menCoachingMenSports))
print("Number of Women's Sports Coached by Men: " + str(menCoachingWomenSports))
print("Number of Men's Sports Coached by Women: " + str(womenCoachingMenSports))
print("Number of Women's Sports Coached by Women: " + str(womenCoachingWomenSports))

# summaryDataFrame = pd.DataFrame(data = {'Men\'s Sports': [menCoachingMenSports, womenCoachingMenSports], 'Women\'s Sports': [menCoachingWomenSports, womenCoachingWomenSports], 'Overall': [menCoaches, womenCoaches]})
# summaryDataFrame.index = ['Man Head Coach', 'Woman Head Coach']
# summaryDataFrame.to_csv("data/summary_stats.csv")

menSportManCoachPercentage = round((menCoachingMenSports/numMenSports) * 100, 2)
menSportWomanCoachPercentage = round((womenCoachingMenSports/numMenSports) * 100, 2)

womenSportManCoachPercentage = round((menCoachingWomenSports/numWomenSports) * 100, 2)
womenSportWomanCoachPercentage = round((womenCoachingWomenSports/numWomenSports) * 100, 2)

totalWomenCoachPercentage = round(((womenCoachingMenSports + womenCoachingWomenSports)/numTotalSports) * 100, 2)
totalMenCoachPercentage = round(((menCoachingMenSports + menCoachingWomenSports)/numTotalSports) * 100, 2)


summaryDataFrame = pd.DataFrame(data = { 'Sport Gender': ['Men\'s Sports', 'Men\'s Sports', 'Women\'s Sports', 'Women\'s Sports', 'Overall', 'Overall'], 'Coach Gender': ['Woman', 'Man', 'Woman', 'Man', 'Woman', 'Man'], 'Number': [womenCoachingMenSports, menCoachingMenSports, womenCoachingWomenSports, menCoachingWomenSports, womenCoaches, menCoaches], 'Percentage': [menSportWomanCoachPercentage, menSportManCoachPercentage, womenSportWomanCoachPercentage, womenSportManCoachPercentage, totalWomenCoachPercentage, totalMenCoachPercentage] })
summaryDataFrame.to_csv("data/summary_stats.csv", index=False)
