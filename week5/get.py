import requests

url = 'https://api.samplicio.us/Demand/v1/Surveys/BySurveyNumber/{SurveyNumber}'

headers = {'Authorization' : YOUR_API_KEY_HERE}

response = requests.get(url, headers=headers)