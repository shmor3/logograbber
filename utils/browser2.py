import requests, os
from dotenv import load_dotenv
import urllib.parse
from bs4 import BeautifulSoup
import re

load_dotenv()

headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'referer': 'https://duckduckgo.com/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"', 
'sec-ch-ua-mobile': '?0', 
'sec-ch-ua-platform': '"macOS"', 
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'}


data = requests.get('http://duckduckgo.com/html/?q=' + urllib.parse.quote_plus(str(os.environ['keyword']) + ' ' + str(os.environ['advQuery'])), headers=headers)
parsed = BeautifulSoup(data.content)

first_link = parsed.findAll('div', {'class': re.compile('links_main*')})[0].a['href']
print(first_link)
# for i in parsed.findAll('div', {'class': re.compile('links_main*')}): 
#     print(i.a['href'])