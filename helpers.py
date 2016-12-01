
import pandas as pd
import json

class Plant():

    def __init__(self, lat=None, lon=None, name=None, owner=None, group=None, output=None, source=None):
        self.lat = lat
        self.lon = lon
        self.name = name
        self.system_owner_name = owner

        self.aer_fuel_type = [] #list of aggregated fuel types
        self.reported_fuel_type = [] #full list of reported fuel types
        self.fuel_groups = {} #key : fuel group (i.e. coal, petrolium)
                              #value: fuel cost, cents/billion BTU
        
        self.output = {} #Key: AER Fuel Type
                         #Value: Power Output to date in MegaWattHours
        #Net generation, year to date in megawatthours (MWh).Numeric. This is total electrical output net of station service.  In the case of combined heat and power plants, this value is intended to include internal consumption of electricity for the purposes of a production process, as well as power put on the grid.

        self.energy_source = ""






# def get_plant_locs():




#"""
#FOR Lat/Long


locs = {} # key : plant id
          # value: (latitude, longitude, name) tuple
path = "eia8602015/"
filename = "2___Plant_Y2015.xlsx"
xl = pd.ExcelFile(path + filename)
data = xl.parse(xl.sheet_names[0], skiprows=[0])

for idx, row in data[['Plant Code', 'Latitude', 'Longitude', 'Plant Name', "Transmission or Distribution System Owner"]].iterrows():
    locs.setdefault(row['Plant Code'], Plant(lat=row['Latitude'], lon=row['Longitude'], name=row['Plant Name'], owner=row["Transmission or Distribution System Owner"]))


#"""

path = "f923_2015/"
filename = "EIA923_Schedules_2_3_4_5_M_12_2015_Final.xlsx"

xl = pd.ExcelFile(path+filename)
data = xl.parse(xl.sheet_names[0], skiprows = range(5))

for idx, row in data[['Plant Id', 'AER\nFuel Type Code', 'Reported\nFuel Type Code', 'Net Generation\n(Megawatthours)']].iterrows():
    plant = locs.get(row['Plant Id'])
    aer = row['AER\nFuel Type Code']
    reported = row['Reported\nFuel Type Code']
    total_output = row['Net Generation\n(Megawatthours)']
    if(plant is not None):
        if aer not in plant.aer_fuel_type:
            plant.aer_fuel_type.append(aer)
        if reported not in plant.reported_fuel_type:
            plant.reported_fuel_type.append(reported)
        plant.output[aer] = plant.output.get(aer, 0) + total_output



with open("tsv/plants.json", "w") as f:
    data = [json.dumps(plant.__dict__) for plant in locs.values()]
    f.write(",".join(data));


# get_plant_locs()

