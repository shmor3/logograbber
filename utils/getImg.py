import os, requests, shutil, time, lxml
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()
urlListPath = str(os.environ['urlListDir'])
urlList = tuple(open(urlListPath, 'r'))
class getImg():
    def opera():
        for url in urlList:
            try:
                urlfrrm = str(url)
                baseUrl = str(os.environ['baseUrl'])
                url = str(os.environ['baseUrl']) + str(os.environ['urlEnding']) + urlfrrm
                output_dir = os.environ['dlDir']     
                time.sleep(1)
                page = requests.get(url, stream = True)
                soup = BeautifulSoup(page.content, 'html.parser')
                souf = soup.find(os.environ['type'], alt=os.environ['altTag'])
                imgUrl = baseUrl + souf.attrs['src'].replace('..', '')
                filename = imgUrl.split("/")[-1]
                print('Image Found')
                time.sleep(1)
                r = requests.get(imgUrl, stream = True)
                if r.status_code == 200:
                    r.raw.decode_content = True
                    with open(filename,'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                        moV = shutil.move(str(filename), output_dir)
                        print(u'\n\u001b[32mDownloaded Successfully\n')
                    pass
                else:
                    print(u'\n\u001b[31mDownload Failed\n')
                    pass
            except OSError as e:
                print('Critical Error', e)
    opera()
getImg()