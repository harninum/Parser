import requests
import fake_useragent
from bs4 import BeautifulSoup

user = fake_useragent.UserAgent().random
header = {'user-agent': user}

link = 'https://browser-info.ru/'
response = requests.get(link, headers=header).text
soup = BeautifulSoup(response, 'lxml')
block = soup.find('div', id="tool_padding")

#Check Js
check_js = block.find('div', id='javascript_check')
status_js = check_js.find_all('span')[1].text
result_js = f'javascript: {status_js}'

#Check Flash
check_fl = block.find('div', id='flash_version')
status_fl = check_fl.find_all('span')[1].text
result_fl = f'flash: {status_fl}'

#Check User-Agent
chek_user = block.find('div', id='user_agent').text
result_user = f'User-Agent: {chek_user}'

print(result_js)
print(result_fl)
print(chek_user)