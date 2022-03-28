import requests, os, re, urllib.parse, lxml, csv
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

headers = {'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'referer': 'https://duckduckgo.com/',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"', 
'sec-ch-ua-mobile': '?0', 
'sec-ch-ua-platform': '"macOS"', 
'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36'}

list_cities_id = []
class DDG():
    def search():
        with open('../data/lists.source/cities.csv') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                included_cols = [1]
                for row in spamreader:
                    content = list(row[i] for i in included_cols)
                    list_cities_id.append(content)

        for city in list_cities_id[1:10]:
            #str(os.environ['keyword'])
            data = requests.get('http://duckduckgo.com/html/?q=' + urllib.parse.quote_plus(city[0] + ' ' + str(os.environ['advQuery'])), headers=headers)
            parsed = BeautifulSoup(data.content, 'lxml')

            first_link = parsed.findAll('div', {'class': re.compile('links_main*')})[0].a['href']
            print(city[0], first_link)
    search()
DDG()
# for i in parsed.findAll('div', {'class': re.compile('links_main*')}): 
#     print(i.a['href'])



        # filepath = str(os.environ['keywordList'])
        # with open(filepath) as fp:
        #     line = fp.readline()
        #     cnt = 1
        #     while line:
        #         line = fp.readline()
        #         cnt += 1