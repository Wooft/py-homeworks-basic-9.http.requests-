import requests
from ya_di import YandexDisk
from pprint import pprint

if __name__ == '__main__':
    TOKEN = "AQAAAAAFC3KFAADLW3RpNV5khk3NkfJZ2ZzJ80w"
    ya = YandexDisk(token=TOKEN)
    ya.up_file(disk_file_path ='Netology/1.jpg',
               filename='1.jpg')
