import json

with open('survey.json') as infile:
    data = json.load(infile)
    print(data)

