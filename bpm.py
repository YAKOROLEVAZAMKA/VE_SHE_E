import requests
import json
from pandas.io.json import json_normalize

url = 'https://bpm.nearmedic.ru/ServiceModel/AuthService.svc/Login'

LOGIN = "Supervisor"
PASSWORD = "Nearmedicph" 

res = requests.post(url, json={"UserName":LOGIN, "UserPassword":PASSWORD})
#print(res.text)
df = res.text

d = json.loads(df)
df2 = json_normalize(d)
code = df2.iloc[0]['Code']
message = df2.iloc[0]['Message']

if code == 0:
    print('OK')
else:
    print(message)
