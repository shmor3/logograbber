import os, requests, shutil
from bs4 import BeautifulSoup
from dotenv import load_dotenv

def getImg():
    load_dotenv()
    url = os.environ['url']
    base_url = os.environ['base_url']
    output_dir = '../data/tmp/todo'
    page = requests.get(url, stream = True, headers={"User-agent": "Mozilla/5.0"})
    soup = BeautifulSoup(page.content, 'html.parser')
    souf = soup.find('img', alt='[City Seal]')
    img_url = base_url + souf.attrs['src'].replace('..', '')
    filename = img_url.split("/")[-1]

    r = requests.get(img_url, stream = True)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            moV = shutil.move(str(filename), output_dir)
    else:
        print('fail')
getImg()