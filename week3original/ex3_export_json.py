from example_data import lucid_codes
import json

with open('output.json', 'w') as outfile:
    json.dump(lucid_codes, outfile)
