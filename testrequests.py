import urllib.request, json
url = urllib.request.urlopen("http://127.0.0.1:5000")
data = json.loads(url.read())
print(data[0]['city_name'])
