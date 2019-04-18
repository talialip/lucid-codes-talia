import requests, json

url = 'https://sandbox.techops.engineering/Demand/v1/Surveys/Create'
params = {
    "SurveyStatusCode": "01",
    "SurveyPriority": 11,
    "SurveyName": "Example API Survey",
    "CountryLanguageID": 9,
    "IndustryID": 30,
    "StudyTypeID": 1,
    "ClientCPI": 1,
    "QuotaCPI": 2,
    "ClientSurveyLiveURL": "https://www.surveyURL.com?rid=[%RID%]",
    "TestRedirectURL": "https://www.surveyURL.com?rid=[%RID%]",
    "IsActive": True,
    "Quota": 1000,
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
    "BusinessUnitID": 125,
    "SampleTypeID": 100,
    "BidIncidence": 20,
    "CollectsPII": None
 }
data = json.dumps(params)
headers = {'Content-type': 'application/json', 'Authorization' : 'AAAD8C59-0004-4AF5-8744-98EFAF195293', 'Accept': 'text/plain'}
response = requests.post(url, data=data, headers=headers)
print(response.content.decode())