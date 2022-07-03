import requests
from ya_di import YandexDisk
from pprint import pprint

TOKEN = "AQAAAAAFC3KFAADLW3RpNV5khk3NkfJZ2ZzJ80w"

ya = YandexDisk(token = TOKEN)
pprint(ya.get_file_list())