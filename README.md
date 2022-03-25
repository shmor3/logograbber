# govlogopy
Python Web Crawler + Auto Data Entry Script

# imports
- CSV
- Pandas
- Pillow
- Selenium
- BeautifulSoup

installation:

```
pip3 install requests bs4 Pillow google python-dotenv
```

Usage:

Starts Full Scripts
```
python3 sealsnatcher.py
```

Resizes All Images And Converts To .PNG
Place Images in '/data/todo' Exports to '/data/done' After Script Runs
```
python3 resize.py
```
Send Web Requests, Finds Image, Then Downloads Images
```
python3 getImg.py
````

Specify Operating System Executable for Chrome Driver
Options:
    - chromedriver              //Linux
    - chromedriver-osx          //OSX
    - chromedriver.exe          //Windows

```
   driver = webdriver.Chrome(executable_path=r"./chromedriver-osx")
```

.env sample
```
proxyTestUrl=https://ipecho.net/plain
url_ending=
base_url=https://www.crwflags.com
advQuery=site:www.crwflags.com inurl:/fotw/flags/
keywordList=./data/cities
width=150
height=150
saveImgAs=.png
src=src
alt=[City Seal]
img=img
DL_Dir=./tmp/todo
done=./tmp/done
proxyList=./data/proxy
```