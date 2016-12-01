
import pandas as pd
import json

class Plant():

    def __init__(self, lat, lon, name):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.fuel_groups = {} #key : fuel group (i.e. coal, petrolium)
                              #value: fuel cost, cents/billion BTU
        self.aer_fuel_type = {}




# df = xl.parse("Sheet1")
# df.head()

# def get_plant_locs():
locs = {} # key : plant id
          # value: (latitude, longitude, name) tuple
path = "eia8602015/"
filename = "2___Plant_Y2015.xlsx"
xl = pd.ExcelFile(path + filename)
data = xl.parse(xl.sheet_names[0], skiprows=[0])

for idx, row in data[['Plant Code', 'Latitude', 'Longitude', 'Plant Name']].iterrows():
    locs.setdefault(row['Plant Code'], Plant(row['Latitude'], row['Longitude'], row['Plant Name']))


path = "f923_2015/"
filename = "EIA923_Schedules_2_3_4_5_M_12_2015_Final.xlsx"

xl = pd.ExcelFile(path+filename)
data = xl.parse(xl.sheet_names[5], skiprows = range(5))

print locs   


with open("tsv/plants.json", "w") as f:
    data = [json.dumps(plant.__dict__) for plant in locs.values()]
    f.write(",".join(data));



# get_plant_locs()

