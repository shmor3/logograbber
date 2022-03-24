import os, requests, time
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
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
                search_result = list(search(query, tld="co.in", num=1, stop=2, pause=1))

                time.sleep(1)

                page = requests.get(search_result[0])
                tree = html.fromstring(page.content)
                soup = BeautifulSoup(page.content, features="lxml")
                os.putenv("url_ending", search_result[0].replace('https://www.crwflags.com/fotw',''))
    search()
browser()
