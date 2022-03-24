import os, requests, time
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
proxies = {
    'http://93.117.72.27:43631'
    'http://200.105.215.18:33630',
    'http://8.214.41.50:80',
    'http://63.151.67.7:8080',
    'http://103.148.72.192:80',
    'http://77.236.238.179:8080',
    'http://45.172.108.39:999',
    'http://46.209.30.12:8080',
    'http://62.75.229.155:5566'
    }

class browser():
    def search():
        filepath = str(os.environ['list'])
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                line = fp.readline()
                cnt += 1
        query = '{}'.format(line.strip()) + ' ' + str(os.environ['advQuery'])
        search_result = list(search(query, tld="co.in", num=1, stop=3, pause=2.0))
        print(proxies)
        page = requests.get('https://ipecho.net/plain', stream = True, headers={"User-agent": "Mozilla/5.0"}, proxies={"http": proxies, "https": proxies})
        tree = html.fromstring(page.content)
        soup = BeautifulSoup(page.content, features="lxml")
    search()
browser()
