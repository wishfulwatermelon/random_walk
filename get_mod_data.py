import requests

def get_mod_data(mod_code):
    return requests.get("https://api.nusmods.com/v2/2020-2021/modules/"+ mod_code +".json").json()
