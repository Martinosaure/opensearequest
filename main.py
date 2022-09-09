import requests
import json



url = 'https://api.opensea.io/api/v1/asset/0x8a90cab2b38dba80c64b7734e58ee1db38b8992e/1094/'
headers = {
    "Accept": "application/json",
    "X-API-KEY": ""
}
r = requests.get(url, headers=headers,)
data = r.json()['collection']

# data = r.json()['average_price'] -> Returns  data = r.json()['average_price'] KeyError: 'average_price'

print(data)
