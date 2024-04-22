import requests
import csv
import time
import os


steam_spy_url = "https://steamspy.com/api.php"
base_steam_url = "https://store.steampowered.com/api/appdetails"
appid_url = "http://api.steampowered.com/ISteamApps/GetAppList/v0002/"

with open('src/page.txt', 'r') as file:
    content = file.read()
    page = int(content)

appid = 0 # will change

steam_spy_param = {"request": "all", "page": page}
base_steam_param = {"appids": appid, 'l': 'english'}
appid_param = {"key": "STEAMKEY", "format": "json"}

appid_json = (requests.get(url=appid_url, params=appid_param)).json()

appid_dict_list = (appid_json['applist'])['apps']

applist = []

# for app_dict in appid_dict_list:
#     applist.append(app_dict['appid'])

# for i in range(50):
#     applist.append(app_dict['appid'])

# for app in applist:
#     rahh



path = 'data/spydata.csv'
spycsvheader = ['appid','name','developer','positive','negative','owners','ccu','initialprice']
try:
    if not os.path.isfile(path): # add header and write mode 

        with open(path, 'w', encoding='utf-8', newline='') as f: 
            writer = csv.writer(f)
            writer.writerow(spycsvheader)

            fails = 0
            while True:
                print("Page: ", page)

                spy_data = (requests.get(url=steam_spy_url, params={"request": "all", "page": page}))
                if spy_data.status_code == 429:
                    print('Rate limited! please wait')

                if spy_data.status_code != 200 and fails == 0:
                    print("Request failed, retrying")
                    fails += 1
                    time.sleep(2)
                elif spy_data.status_code != 200 and fails != 0:
                    print("Request failed again, stopping requests")
                    break
                else:
                    spy_json = spy_data.json()
                    for app in spy_json:
                        dict = spy_json[app]
                        wanted = [dict['appid'], dict['name'], dict['developer'], dict['positive'], dict['negative'], dict['owners'], dict['ccu'], dict['initialprice']]
                        print(wanted)
                        writer.writerow(wanted)
                    page += 1
    else:
        with open(path, 'a', encoding='utf-8', newline='') as f: 
            writer = csv.writer(f)

            fails = 0
            while True:
                print("Page: ", page)

                spy_data = (requests.get(url=steam_spy_url, params={"request": "all", "page": page}))
                if spy_data.status_code == 429:
                    print('Rate limited! please wait')

                if spy_data.status_code != 200 and fails == 0:
                    print("Request failed, retrying")
                    fails += 1
                    time.sleep(2)
                elif spy_data.status_code != 200 and fails != 0:
                    print("Request failed again, stopping requests")
                    break
                else:
                    spy_json = spy_data.json()
                    for app in spy_json:
                        dict = spy_json[app]
                        wanted = [dict['appid'], dict['name'], dict['developer'], dict['positive'], dict['negative'], dict['owners'], dict['ccu'], dict['initialprice']]
                        print(wanted)
                        writer.writerow(wanted)
                    page += 1
    with open('src/page.txt', 'w') as file:
        file.write(str(page))
except:
    with open('src/page.txt', 'w') as file:
        file.write(str(page))

int = 0
for appid in appid_dict_list:
    
    print(int, " : ", appid)
    int += 1


