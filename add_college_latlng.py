import pandas as pd
# https://geocoder.readthedocs.io/
import geocoder

coaches = pd.read_csv("data/coaches_with_school_addresses.csv")

# g = geocoder.arcgis("College of Charleston (South Carolina)")
# print(g.json)

schoolNames = coaches["School"]
uniqueSchoolNames = set(schoolNames)

schoolLats = {}
schoolLngs = {}
for school in uniqueSchoolNames:
    g = geocoder.arcgis(school)
    schoolLats[school] = g.lat
    schoolLngs[school] = g.lng


schoolLats_df = pd.DataFrame(list(schoolLats.items()), columns = ['School', 'Latitude'])
schoolLngs_df = pd.DataFrame(list(schoolLngs.items()), columns = ['School', 'Longitude'])

schoolLatLng = schoolLats_df.merge(schoolLngs_df, on='School')
schoolLatLng.to_csv("data/school_latlng.csv")

coachesWithSchoolLatLng = coaches.merge(schoolLatLng, on="School", how="left")
coachesWithSchoolLatLng.to_csv("data/coaches_with_latlng")
