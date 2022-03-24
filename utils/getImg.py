import os, requests, shutil, time
from bs4 import BeautifulSoup
from dotenv import load_dotenv

class getImg():
    def opera():
        load_dotenv()
        base_url = os.environ['base_url']
        url = os.environ['base_url'] + os.environ['url_ending']
        output_dir = os.environ['DL_Dir']        
        page = requests.get(url, stream = True, headers={"User-agent": "Mozilla/5.0"})
        soup = BeautifulSoup(page.content, 'html.parser')
        souf = soup.find(os.environ['img'], alt=os.environ['alt'])
        img_url = base_url + souf.attrs[os.environ['src']].replace('..', '')
        filename = img_url.split("/")[-1]
        print('Image Found')
        r = requests.get(img_url, stream = True)
        if r.status_code == 200:
            r.raw.decode_content = True
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)
                moV = shutil.move(str(filename), output_dir)
                print('Download Successfully')
        else:
            pass
    opera()
getImg()