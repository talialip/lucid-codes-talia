import requests, json

url = 'https://api.samplicio.us/Demand/v1/SurveyQualifications/Create/{SurveyNumber}'
params = {
    "Name": "STANDARD_RELATIONSHIP",
    "QuestionID": 632,
    "LogicalOperator": "OR",
    "NumberOfRequiredConditions": 1,
    "IsActive": True,
    "PreCodes": [
        "1"
    ],
    "Order": 7
}
data = json.dumps(params)
headers = {'Content-type': 'application/json', 'Authorization' : 'YOUR_API_KEY_HERE', 'Accept': 'text/plain'}