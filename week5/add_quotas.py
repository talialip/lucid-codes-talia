import requests, json

url = 'https://api.samplicio.us/Demand/v1/SurveyQuotas/Create/{SurveyNumber}'
params = {'Name': 'Quota Name', 'Quota': 50, 'IsActive': True, 'Conditions':[{'QuestionID':42, 'PreCodes': ['18','19','20','21','22'] }]}
data = json.dumps(params)
headers = {'Content-type': 'application/json', 'Authorization' : 'YOUR_API_KEY_HERE', 'Accept': 'text/plain'}

response = requests.post(url, data=data, headers=headers)
