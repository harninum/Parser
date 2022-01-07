import requests
import fake_useragent
from bs4 import BeautifulSoup

url = 'https://www.ozon.ru/'

user = fake_useragent.UserAgent().random
header = {'user-agent': user}


with requests.session() as se:
    se.headers = {
        'User-agent': user
    }





