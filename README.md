# govlogopy
Python Web Crawler + Auto Data Entry Script

# imports
- CSV
- Pandas
- Pillow
- Selenium
- BeautifulSoup

Usage:

Starts Full Scripts
```
python3 logoSnatcher.py
```

Resizes All Images And Converts To .PNG
Place Images in '/data/todo' Exports to '/data/done' After Script Runs
```
python3 resize.py
```

Specify Operating System Executable for Chrome Driver
Options:
    - chromedriver              //Linux
    - chromedriver-osx          //OSX
    - chromedriver.exe          //Windows

```
   driver = webdriver.Chrome(executable_path=r"./chromedriver-osx")
```