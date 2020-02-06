import urllib.request, json, requests
# print(data)
# data[2]['id'] = None
# payload = data[2]
# data = {
# 	"id": "a03"
# }
headers = {'Content-Type':'application/json'}
# print(json.dumps(payload))
# response = requests.post('https://webtask.azurewebsites.net/api/employees/', json.dumps(data),headers=headers)
response = requests.delete('https://webtask.azurewebsites.net/api/employees/a03',headers=headers)