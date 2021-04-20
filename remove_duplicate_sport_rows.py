import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)

coaches = pd.read_csv("data/coaches_with_latlng.csv")

allSports = coaches["Sport"]
schools = coaches["School"]
coachingPeriod = coaches["Period"]

curSchool = ""
sportsAtSchool = {}
duplicatesToDrop = []
for i in range(len(coachingPeriod)):
    if schools[i] != curSchool:
        curSchool = schools[i]
        sportsAtSchool = {}
    # If we've already seen this sport, drop the coach that is not current
    if allSports[i] in sportsAtSchool.keys():
        conflictingSportPeriod1 = coachingPeriod[sportsAtSchool[allSports[i]]].split("-")
        conflictingSportPeriod2 = coachingPeriod[i].split("-")
        if conflictingSportPeriod1[1] == " ":
            duplicatesToDrop.append(i)
        else:
            duplicatesToDrop.append(sportsAtSchool[allSports[i]])
        # print("Duplicate: " + allSports[i] + ", " + curSchool)
        continue
    # Keep track of index of row for the sport in case duplicate is found
    sportsAtSchool[allSports[i]] = i
# Drop duplicates
coaches.drop(duplicatesToDrop, inplace=True)

coaches.to_csv("data/coaches_duplicate_sports_removed.csv", index=False)
