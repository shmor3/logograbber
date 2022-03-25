import os, requests, shutil, time
from bs4 import BeautifulSoup
from dotenv import load_dotenv

class getImg():
    def opera():
        load_dotenv()
        filepath = str(os.environ['urlListDir'])
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                line = fp.readline()
                cnt += 1
                baseUrl = str(os.environ['baseUrl'])
                url = str(os.environ['baseUrl']) + str(os.environ['urlEnding']) + str('{}'.format(line.strip()))
                output_dir = os.environ['dlDir']     
                time.sleep(1)
                page = requests.get(url, stream = True, headers={"User-agent": "Mozilla/5.0"})
                soup = BeautifulSoup(page.content, 'html.parser')
                souf = soup.find(os.environ['img'], alt=os.environ['alt'])
                img_url = baseUrl + souf.attrs[os.environ['src']].replace('..', '')
                filename = img_url.split("/")[-1]
                print('Image Found')
                time.sleep(1)
                r = requests.get(img_url, stream = True)
                if r.status_code == 200:
                    r.raw.decode_content = True
                    with open(filename,'wb') as f:
                        shutil.copyfileobj(r.raw, f)
                        moV = shutil.move(str(filename), output_dir)
                        print(u'\u001b[32mDownloaded Successfully\n')
                else:
                    print(u'\u001b[31mDownload Failed\n')
                    pass
    opera()
getImg()