import pandas as pd

coaches = pd.read_csv("data/coaches_with_latlng.csv")
coachGenders = coaches["gender"]
sports = coaches["Sport"]
coachGenderSportGender = []
for i in range(len(coachGenders)):
    if "Men" in sports[i] or sports[i] in ["Football", "Baseball"]:
        coachGenderSportGender.append((coachGenders[i], "men"))
    if "Women" in sports[i] or sports[i] in ["Field Hockey", "Softball"]:
        coachGenderSportGender.append((coachGenders[i], "women"))


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
