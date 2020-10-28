import requests
import json 

url = 'http://127.0.0.1:5000/'
data = {'data': 'Jag hatar dig'}
data = json.dumps(data)
send = requests.post(url, data)
ans=send.json()

print(ans)