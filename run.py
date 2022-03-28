import time, os, requests, shutil, glob, re, lxml, csv, urllib.parse
from googlesearch import search
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from PIL import Image

load_dotenv()
class sealsnatcher():
    def search():
        proxiesList = tuple(open(str(os.environ['proxyList']), 'r'))
        for proxy in proxiesList:
            try:
                proxyfrrm = 'http://' + str(proxy)
                print(u'\n\u001b[33mChecking Proxy:\n', proxyfrrm)
                time.sleep(1)
                proxPage = requests.get(os.environ['proxyTestUrl'])
                time.sleep(1)
                print(u'\n\u001b[32mStatus',proxPage.status_code,'OK','PASS:\n', '\u001b[36;1mProxy IP', proxPage.text)
            except OSError as e:
                print(u'\n\u001b[31mStatus',e,'FAIL:\n', proxyfrrm, '\u001b[0m\n')
                with open(os.environ['proxyList'], "r+") as f:
                    d = f.readlines()
                    f.seek(0)
                    for i in d:
                        if i != str(proxy):
                            f.write(i)
                            f.truncate()
        keyWordList = tuple(open(str(os.environ['keywordList']), 'r'))
        for keyWord in keyWordList:
            try:
                query = keyWord + ' ' + str(os.environ['advQuery'])
                print(u'\n', '\u001b[32m@' + 'google.com|' + str(query), '\n\u001b[36;1mSearching:', '\u001b[33m')
                search_result = list(search(query, tld="com", num=1, stop=1, pause=10))
                time.sleep(1)
                page = requests.get(search_result[0])
                search.u = str(search_result[0]).replace('https://www.crwflags.com/fotw/flags/', '')
                print(u'\n\u001b[32mStatus', page.status_code, 'OK', 'PASS')
                urlList = open(os.environ['urlListDir'], "a")
                urlList.write(str(search.u).replace('https://www.crwflags.com/fotw/flags/','')+'\n')
                urlList.close()
            except:
                print('SEARCH ERROR')
    search()
    def dlImg():
        urlList = tuple(open(str(os.environ['urlListDir']), 'r'))
        for url in urlList:
            try:
                dlDir = os.environ['tmpDir']
                os.makedirs(dlDir, exist_ok=True)
                baseUrl = os.environ['baseUrl']
                urlRoute = os.environ['urlRoute']
                localUrl = os.environ['localUrl']
                localRoute = os.environ['localRoute']
                urlr = localUrl.lower() + localRoute + url.replace('.html', ').gif')
                urlp = baseUrl.lower() + urlRoute + url
                page = requests.get(urlp)
                time.sleep(1)
                soup = BeautifulSoup(page.content, 'lxml')
                soupd = soup.find('img', alt='[City Seal]')
                soupf = soupd.attrs['src'].replace('../', '')
                imgUrl = urlr.replace(url, '')
                filename = imgUrl.split("/")[-1]
                time.sleep(1)
                r = requests.get(imgUrl, stream = True)
                time.sleep(1)
                if r.status_code == 200:
                    r.raw.decode_content = True
                    with open(filename,'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                        moV = shutil.move(str(filename), dlDir)
                        print(u'\n\u001b[32mDownloaded Successfully')
                        with open(os.environ['urlListDir'], "r+") as f:
                            d = f.readlines()
                            f.seek(0)
                            for i in d:
                                if i != str(url):
                                    f.write(i)
                                    f.truncate()
                    pass
                else:
                    print(u'\n\u001b[31mDownload Failed')
                    pass
            except:
                print('DOWNLOAD ERROR')
    dlImg()
    def sizeImg():
        dst_dir = str(os.environ['done'])
        os.makedirs(dst_dir, exist_ok=True)
        files = glob.glob(str(os.environ['tmpDir'] + '/*'))
        for f in files:
            try:
                img = Image.open(f)
                img_resize = img.resize((int(os.environ['width']), int(os.environ['height'])))
                root, ext = os.path.splitext(f)
                basename = os.path.basename(root)
                imgName = os.path.join(dst_dir, basename + os.environ['saveImgAs'])
                img_resize.save(imgName)
                print(u'\n\u001b[32mResize Successful')
            except OSError as e:
                print('RESIZE ERROR')
                pass
    sizeImg()
    def cleanUpDir():
        folder = os.environ['tmpDir']
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print('\n\u001b[32mCleanup Successful\n')    
            except Exception as e:
                print(u'\n\u001b[31mCleanup Failed\n')
                pass
    cleanUpDir()
sealsnatcher()