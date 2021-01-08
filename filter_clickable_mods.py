import requests

# need to check if modules are clickable

def check_clickable(mod):
    if requests.get("https://api.nusmods.com/v2/2020-2021/modules/"+ mod +".json").status_code != 200:
        return False
    mod_data = requests.get("https://api.nusmods.com/v2/2020-2021/modules/"+ mod +".json").json()
    return mod_data['semesterData']

def only_clickable(mod_list):
    return list(filter(lambda x: check_clickable(x), mod_list))