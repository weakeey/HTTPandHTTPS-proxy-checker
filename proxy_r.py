import requests
from bs4 import BeautifulSoup
import fake_useragent
import re

user = fake_useragent.UserAgent().random

with open('proxy.txt') as file:
    proxys = ''.join(file.readlines()).strip().split('\n')

for proxy in proxys:
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }

    url = 'https://icanhazip.com/'
    
    try:
        responce = requests.get(url, proxies=proxies, timeout=2).text
        print(f'IP: {responce}')
    except:
        print('Прокси не валидный')