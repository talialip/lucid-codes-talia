import json

with open('output.json') as infile:
    data = json.load(infile)
    #print(data)

print(data['ResultCount'])