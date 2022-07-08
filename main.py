import requests
from ya_di import YandexDisk
from ya_di import YaUploader
from pprint import pprint

def get_hero_id():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    sup_d = {}
    sup_d = response.json()
    l_hero = ['Hulk', 'Captain America', 'Thanos']
    l_id = {}
    for names in l_hero:
        for elements in sup_d:
            for keys, values in elements.items():
                if values == names:
                    l_id[names] = elements['id']
    return l_id

def get_hero_maxint():
    l_id = get_hero_id()
    h_int = {}
    for keys, values in l_id.items():
        url_s = f'https://akabab.github.io/superhero-api/api/powerstats/{values}.json'
        response = requests.get(url_s)
        h_int[keys] = response.json()['intelligence']
    res_dict = dict([max(h_int.items(), key=lambda k_v: k_v[1])])
    return res_dict

pprint(f'Самый умный: {get_hero_maxint()}')

if __name__ == '__main__':
    path_to_file = '/home/wooft/PycharmProjects/py-homeworks-basic_9.http.requests/1.jpg'
    TOKEN = "AQAAAAAFC3KFAADLW3RpNV5khk3NkfJZ2ZzJ80w"
    uploader = YaUploader(token=TOKEN)
    uploader.upload(path_to_file)