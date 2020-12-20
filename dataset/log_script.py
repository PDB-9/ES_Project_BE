import json
from collections import Counter
infile = r"..\logs\app.log"
data_searched = []
with open(infile) as f:
    f = f.readlines()
    for line in f:
        result = json.loads(line)
        json_data= result['INFO']
        for data in json_data:
            search_data= result['INFO'][data]["request"]["data"]
            if search_data!={}:
                data_searched.append(search_data['search'])
print(Counter(data_searched))