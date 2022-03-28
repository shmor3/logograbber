import os, requests, time
from googlesearch import search
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
prxyPth = str(os.environ['proxyList'])
proxiesList = tuple(open(prxyPth, 'r'))
class browser():
    def search():
        for proxy in proxiesList:
            try:
                proxyfrrm = 'http://' + str(proxy)
                print(u'\n\u001b[33mChecking Proxy:\n', proxyfrrm)
                time.sleep(1)
                proxPage = requests.get(os.environ['proxyTestUrl'], proxies = {"http": proxyfrrm, "https": proxyfrrm})
                time.sleep(1)
                print(u'\n\u001b[32mStatus',proxPage.status_code,'OK','PASS:\n', '\u001b[36;1mProxy IP', proxPage.text)
                pass
            except OSError as e:
                print(u'\n\u001b[31mStatus',e,'FAIL:\n', proxyfrrm, '\u001b[0m\n')
                with open(prxyPth, "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != str(proxy):
                            f.write(i)
                            f.truncate()
        filepath = str(os.environ['keywordList'])
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                line = fp.readline()
                cnt += 1
                try:
                    query = '{}'.format(line.strip()) + ' ' + str(os.environ['advQuery'])
                    print(u'\n', str(proxyfrrm) + ' ->', 'google.com|' + str(query), '\n\u001b[36;1mSearching:', '\u001b[0m|', '\u001b[33m{}\n'.format(line.strip()))
                    search_result = list(search(query, tld="com", num=1, stop=1, pause=10))
                    time.sleep(1)
                    page = requests.get(search_result[0])
                    time.sleep(1)
                    print(u'\n\u001b[32mStatus',page.status_code,'OK','PASS')
                    urlList = open(os.environ['urlListDir'], "a")
                    urlList.write(search_result[0].replace('https://www.crwflags.com/fotw/flags/','')+'\n')
                    urlList.close()
                    print(u'\u001b[32mAdded', '{}'.format(line.strip()))
                except OSError as e:
                    print(u'\n\u001b[31mCritical Error\n', e)
                    browser()
    search()
browser()