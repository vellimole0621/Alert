import json

file_path = "./gps_info.json"

data = {}
data['gps'] = []
data['gps'].append({
    "latitude": "75.6",
    "longitude": "37.5",
})

print(data)

with open(file_path, 'w') as outfile:
    json.dump(data, outfile, indent=4)