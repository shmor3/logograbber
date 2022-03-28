import time, os, requests, shutil, glob, re, lxml, csv, urllib.parse
from googlesearch import search
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from PIL import Image

load_dotenv()
class sealsnatcher():
    def search():
        prxyPth = str(os.environ['proxyList'], proxies={"http": proxyfrrm, "https": proxyfrrm})
        proxiesList = tuple(open(prxyPth, 'r'))
        for proxy in proxiesList:
            try:
                proxyfrrm = 'http://' + str(proxy)
                print(u'\n\u001b[33mChecking Proxy:\n', proxyfrrm)
                time.sleep(1)
                proxPage = requests.get(os.environ['proxyTestUrl'])
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
        query = '{}'.format(line.strip()) + ' ' + str(os.environ['advQuery'])
        print(u'\n', '\u001b[32m@' + 'google.com|' + str(query), '\n\u001b[36;1mSearching:', '\u001b[0m|', '\u001b[33m{}'.format(line.strip()))
        search_result = list(search(query, tld="com", num=1, stop=1, pause=10))
        time.sleep(1)
        page = requests.get(search_result[0], proxies={"http": proxyfrrm, "https": proxyfrrm})
        pageRes = str(search_result[0]).lower
        search.u = str(pageRes).replace('https://www.crwflags.com/fotw/flags/','')+'\n'
        print(u'\n\u001b[32mStatus',page.status_code,'OK','PASS')
    search()
    def dlImg():
        dlDir = os.environ['tmpDir']
        os.makedirs(dlDir, exist_ok=True)
        baseUrl = os.environ['baseUrl']
        target = search.u
        urlRoute = os.environ['urlRoute']
        urlr = baseUrl.lower() + urlRoute + target
        page = requests.get(urlr)
        time.sleep(1)
        soup = BeautifulSoup(page.content, 'lxml')
        soupd = soup.find('img', alt='[City Seal]')
        soupf = soupd.attrs['src'].replace('../', '')
        urly = urlr.replace(target, '')
        imgUrl = urly.replace(str(urlRoute),'') + soupf.lower()
        print(u'\u001b[32m', imgUrl, '\n')
        filename = imgUrl.split("/")[-1]
        time.sleep(1)
        r = requests.get(imgUrl, stream = True)
        time.sleep(1)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                moV = shutil.move(str(filename), dlDir)
                print(u'\n\u001b[32mDownloaded Successfully\n')
            pass
        else:
            print(u'\n\u001b[31mDownload Failed\n')
            pass
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
                print(u'\n\u001b[32mResize Successful\n')
            except OSError as e:
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