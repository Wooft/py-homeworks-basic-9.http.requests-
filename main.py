import requests
from ya_di import YandexDisk
from ya_di import YaUploader
from pprint import pprint

if __name__ == '__main__':
    path_to_file = '/home/wooft/PycharmProjects/py-homeworks-basic_9.http.requests/1.jpg'
    TOKEN = "AQAAAAAFC3KFAADLW3RpNV5khk3NkfJZ2ZzJ80w"
    uploader = YaUploader(token=TOKEN)
    uploader.upload(path_to_file)