import os, time, requests, lxml, re
from bs4 import BeautifulSoup


url = 'https://www.crwflags.com/fotw/flags/us-co-dv.html'
page = requests.get(url)
soup = BeautifulSoup(page.content)
soupd = soup.find('img', alt='[City Seal]')
soupd =

print(u'\u001b[32m', soupd, '\n')