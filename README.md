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
pip3 install csv requests shutil bs4 dotenv Pillow
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