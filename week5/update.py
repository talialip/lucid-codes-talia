import requests, json

url = 'https://api.samplicio.us/Demand/v1/Surveys/Update/{SurveyNumber}'
params = {
    "AccountID": 1,
    "SurveyStatusCode": "01",
    "SurveyPriority": 11,
    "SurveyNumber": 12345,
    "SurveyName": "Example API Survey",
    "CountryLanguageID": 9,
    "IndustryID": 30,
    "StudyTypeID": 1,
    "ClientCPI": 1,
    "QuotaCPI": 2,
    "ClientSurveyLiveURL": "https://www.surveyURL.com?rid=[%RID%]",
    "TestRedirectURL": "https://www.surveyURL.com?rid=[%RID%]",
    "IsActive": True,
    "Quota": 100,
    "FulcrumExchangeAllocation": 0,
    "FulcrumExchangeHedgeAccess": True,
    "IsVerifyCallBack": True,
    "UniquePID": True,
    "UniqueIPAddress": True,
    "IsRelevantID": False,
    "IsDedupe": False,
    "IsGeoIP": False,
    "IsFraudProfile": False,
    "FraudProfileThreshold": 0,
    "IsTrueSample": False,
    "QuotaCalculationTypeID": 1,
    "SurveyPlatformID": 1,
    "BidLengthOfInterview": 10,
    "BusinessUnitID": 9,
    "SampleTypeID": 100,
    "BidIncidence": 20,
    "CollectsPII": None
 }
data = json.dumps(params)
headers = {'Content-type': 'application/json', 'Authorization' : 'YOUR_API_KEY_HERE', 'Accept': 'text/plain'}
response = requests.put(url, data=data, headers=headers)