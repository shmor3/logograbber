import os, requests, time
from lxml import html
from googlesearch import search
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
prxyPth = str(os.environ['proxyList'])
proxies = tuple(open(prxyPth, 'r'))
class browser():
    def search():
        for proxy in proxies:
            try:
                proxyfrrm = 'http://' + str(proxy)
                print(u'\u001b[33mChecking Proxy:\n', proxyfrrm, '\u001b[0m ---> ', str(os.environ['proxyTestUrl']))
                time.sleep(1)
                page = requests.get(os.environ['proxyTestUrl'], proxies={"http": proxyfrrm, "https": proxyfrrm})
                print(u'\u001b[32mStatus OK, PASS:\n', proxyfrrm, '\u001b[36;1m --->', page.text)
            except OSError as e:
                print(u'\u001b[31mStatus -, FAIL:\n', proxyfrrm, '\u001b[0m\n', e)
                with open(prxyPth, "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != str(proxy):
                            f.write(i)
                            f.truncate()
        filepath = str(os.environ['ketwordList'])
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                line = fp.readline()
                cnt += 1
                print(u'--->', proxy, '\u001b[0mSearching:', '\u001b[0m|', '\u001b[33m{}'.format(line.strip()))
                query = '{}'.format(line.strip()) + ' ' + str(os.environ['advQuery'])
                search_result = list(search(query, tld="co.in", num=1, stop=3, pause=2.0))
                time.sleep(1)
                page = requests.get(search_result[0], proxies={"http": proxyfrrm, "https": proxyfrrm}, stream = True, headers={"User-agent": "Mozilla/5.0"})
                tree = html.fromstring(page.content)
                soup = BeautifulSoup(page.content, features="lxml")
                os.putenv("url_ending", search_result[0].replace('https://www.crwflags.com',''))
                print(search_result[0].replace('https://www.crwflags.com','') + str(os.environ['url_ending']))
    search()
browser()
