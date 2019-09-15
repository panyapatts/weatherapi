import urllib.request, json 
with urllib.request.urlopen("https://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22") as url:
    data = json.loads(url.read().decode())
    print(data)
