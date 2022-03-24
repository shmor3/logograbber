
# Import the required Modules
import requests
  
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
url = 'https://ipecho.net/plain'
  
for proxy in proxies:
    try:
        page = requests.get(url, proxies={"http": proxy, "https": proxy})
        print('Status OK, PASS ', page.text)
    except OSError as e:
        print(e)