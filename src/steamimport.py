import requests
import csv
import time
import os

def importdata(mode, applist, appid_index, path): # if mode is w, appid_index should be 0
    try:
        basecsvheader = ['appid','type','genre','metacritic','recommendations']

        with open(path, mode, encoding='utf-8', newline='') as f: 
            writer = csv.writer(f)

            if mode == 'w':
                writer.writerow(basecsvheader)

            for appid in applist[appid_index:]:
                base_data = (requests.get(url="https://store.steampowered.com/api/appdetails", params={"appids": appid, 'l': 'english'}))
                if base_data.status_code == 429:
                    while base_data.status_code == 429:
                        print('Rate limited! please wait')
                        time.sleep(30)
                        base_data = (requests.get(url="https://store.steampowered.com/api/appdetails", params={"appids": appid, 'l': 'english'}))
                elif base_data.status_code != 200:
                    print("Abnormal status code: ", base_data.status_code)
                    base_data = (requests.get(url="https://store.steampowered.com/api/appdetails", params={"appids": appid, 'l': 'english'}))
                    if base_data.status_code != 200:
                        print("Abnormal status code again: ", base_data.status_code)
                        print("Exiting...")
                        raise Exception("Abnormal status code", base_data.status_code)
                print("OK", base_data.status_code, "mode", mode)
                print(base_data.json())
                wanted = readandwrite(base_data, appid)
                writer.writerow(wanted)
                appid_index += 1
                print(wanted)
                print(appid_index)
        with open('src/appid.txt', 'w') as file:
            file.write(str(appid_index))
    except:
        with open('src/appid.txt', 'w') as file:
            file.write(str(appid_index))



def readandwrite(data, appid):
    keys = ['type','genres','metacritic','recommendations']

    base_json = data.json()

    print(appid)

    if base_json[str(appid)]['success'] == False:
        wanted = [appid,'','','','']
    else:
        data = (base_json[str(appid)])['data']

        type = ''
        topgenre = ''
        recommendations = ''
        metacritic = ''

        for key in data:
            if key not in keys:
                continue
            elif key == keys[0]:  # key == type
                type = data[key]
                continue
            elif key == keys[1]:  # key == genre
                topgenre = data[key][0]['description']
                continue
            elif key == keys[2]:  # key == metacritic 
                recommendations = data[key]['score']
                continue
            elif key == keys[3]:  #ket == recommendations
                metacritic = data[key]['total']
                continue
        wanted = [appid, type, topgenre, metacritic, recommendations]

    return wanted



appid_url = "http://api.steampowered.com/ISteamApps/GetAppList/v0002/"

with open('src/appid.txt', 'r') as file:
    content = file.read()
    appid_index = int(content)

appid_param = {"key": "STEAMKEY", "format": "json"}

appid_json = (requests.get(url=appid_url, params=appid_param)).json()

appid_dict_list = (appid_json['applist'])['apps']

applist = []

for app_dict in appid_dict_list:
    applist.append(app_dict['appid'])

print("applist size: ", len(applist))

path = 'data/steamdata.csv'

if not os.path.isfile(path): 
    importdata(mode='w', applist=applist, appid_index=appid_index, path=path) # enter write mode
else:
    importdata(mode='a', applist=applist, appid_index=appid_index, path=path) # enter append mode
