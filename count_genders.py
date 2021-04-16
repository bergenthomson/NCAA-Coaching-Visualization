import pandas as pd

coaches = pd.read_csv("data/coaches_with_latlng.csv")
coachGenders = coaches["gender"]
sports = coaches["Sport"]
coachGenderSportGender = []
numMenSports = 0
numWomenSports = 0
numTotalSports = 0
for i in range(len(coachGenders)):
    if "Men" in sports[i] or sports[i] in ["Football", "Baseball", "Mixed Rifle"]:
        coachGenderSportGender.append((coachGenders[i], "men"))
        numMenSports += 1
    if "Women" in sports[i] or sports[i] in ["Field Hockey", "Softball", "Mixed Rifle"]:
        coachGenderSportGender.append((coachGenders[i], "women"))
        numWomenSports += 1
    numTotalSports += 1


menCoaches = 0
womenCoaches = 0
for g in coachGenders:
    if g == "male":
        menCoaches += 1
    if g == "female":
        womenCoaches += 1

menCoachingMenSports = 0
menCoachingWomenSports = 0
womenCoachingMenSports = 0
womenCoachingWomenSports = 0
for t in coachGenderSportGender:
    if t[0] == "male" and t[1] == "men":
        menCoachingMenSports += 1
    if t[0] == "male" and t[1] == "women":
        menCoachingWomenSports += 1
    if t[0] == "female" and t[1] == "men":
        womenCoachingMenSports += 1
    if t[0] == "female" and t[1] == "women":
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

menSportManCoachPercentage = (menCoachingMenSports/numMenSports) * 100
menSportWomanCoachPercentage = (womenCoachingMenSports/numMenSports) * 100

womenSportManCoachPercentage = (menCoachingWomenSports/numWomenSports) * 100
womenSportWomanCoachPercentage = (womenCoachingWomenSports/numWomenSports) * 100

totalWomenCoachPercentage = ((womenCoachingMenSports + womenCoachingWomenSports)/numTotalSports) * 100
totalMenCoachPercentage = ((menCoachingMenSports + menCoachingWomenSports)/numTotalSports) * 100


summaryDataFrame = pd.DataFrame(data = { 'Sport Gender': ['Men\'s Sports', 'Men\'s Sports', 'Women\'s Sports', 'Women\'s Sports', 'Overall', 'Overall'], 'Coach Gender': ['Man', 'Woman', 'Man', 'Woman', 'Man', 'Woman'], 'Number': [menCoachingMenSports, womenCoachingMenSports, menCoachingWomenSports, womenCoachingWomenSports, menCoaches, womenCoaches], 'Percentage': [menSportManCoachPercentage, menSportWomanCoachPercentage, womenSportManCoachPercentage, womenSportWomanCoachPercentage, totalMenCoachPercentage, totalWomenCoachPercentage] })
summaryDataFrame.to_csv("data/summary_stats.csv", index=False)
