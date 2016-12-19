import json


with open('tsv/plants.json') as data_file:    
    data = json.load(data_file)


types = {
    "SUN" : "Solar",
    "COL" : "Coal",
    "DFO" : "Petroleum",
    "GEO" : "Geothermal",
    "HPS" : "Hydroelectric",
    "HYC" : "Hydroelectric",
    "MLG" : "Natural / Other Gas",
    "NG" : "Natural / Other Gas",
    "NUC" : "Nuclear",
    "OOG" : "Natural / Other Gas",
    "ORW" : "Other",
    "OTH" : "Other",
    "PC" : "Petroleum",
    "RFO" : "Petroleum",
    "WND" : "Wind",
    "WOC" : "Coal",
    "WOO" : "Waste Oil",
    "WWW" : "Wood and Wood Waste"
}

sums = {
"SUN" : 0,
"COL" : 0,
"DFO" : 0,
"GEO" : 0,
"HPS" : 0,
"HYC" : 0,
"MLG" : 0,
"NG" : 0,
"NUC" : 0,
"OOG" : 0,
"ORW" : 0,
"OTH" : 0,
"PC" : 0,
"RFO" : 0,
"WND" : 0,
"WOC" : 0,
"WOO" : 0,
"WWW" : 0
}


for obj in data:
    for key, value in obj['output'].iteritems():
        if key != "":
            sums[key] += value;

vis_data = {}
for (sumkey, sumvalue), (typekey, typevalue) in zip(sums.iteritems(), types.iteritems()):
    vis_data[typevalue] = vis_data.get(typevalue, 0) + sumvalue
    

x = []

for key, value in vis_data.iteritems():
    x.append({
        "name":key,
        "total": "{}".format(round(int(value)/1000000)*1000000),
        "key":""
        })

for entry in x:
    for key,value in types.iteritems():
        if value == entry["name"]:
            entry["key"] = key
            entry.setdefault("keys", []).append(key)



print x

