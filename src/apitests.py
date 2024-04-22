import requests
import csv
import json

steam_spy_url = "https://steamspy.com/api.php"
base_steam_url = "https://store.steampowered.com/api/appdetails"

steam_spy_headers = ['appid', 'name', 'developer', 'publisher', 
                    'score_rank', 'positive', 'negative', 'userscore',
                    'owners', 'average_forever', 'average_2weeks',
                    'median_forever', 'median_2weeks', 'price',
                    'initialprice', 'discount', 'ccu']

base_steam_headers = ['steam_appid', 'type', 'name', 'genres', 'metacritic',
                     'price', 'recommendations', 'developers']


steam_spy_param = {"request": "all", "page": "0"}
base_steam_param = {"appids": "243450", 'l': 'english'}
# base_steam_appids_param = {"appids": }

steam_spy_request = requests.get(url=steam_spy_url, params=steam_spy_param)

steam_spy_json = steam_spy_request.json()

for app in steam_spy_json:
    dict = steam_spy_json[app]
    for key in dict:
        print(dict[key])

    # print(dict['appid'], dict['name'], dict['developer'], dict['positive'], dict['negative'], dict['owners'], dict['ccu'], dict['initialprice'])

# base_steam_request = requests.get(url=base_steam_url, params=base_steam_param)

# base_steam_json = base_steam_request.json()

# innerdict = (base_steam_json['243450'])['data']
# type = innerdict['type']
# topgenre = ((innerdict['genres'])[0])['description']
# recommendations = (innerdict['recommendations'])['total']
# metacritic = (innerdict['metacritic'])['score']

# print(type,topgenre,recommendations,metacritic)

# base_steam_appids_request = requests.get(url=base_steam_url, params=base_steam_appids_param)

# base_steam_appid_json = base_steam_appids_request.json()

# print(base_steam_appid_json)