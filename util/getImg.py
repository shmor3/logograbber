import requests
import shutil
from bs4 import BeautifulSoup

url = 'http://fotw.ethnia.org/flags/us-co-dv.html'

def getImg(url):
    base_url = 'http://fotw.ethnia.org'
    output_dir = '/data/tmp/todo'
    page = requests.get(url, stream = True, headers={"User-agent": "Mozilla/5.0"})
    soup = BeautifulSoup(page.content, 'html.parser')
    souf = soup.find('img', alt='[City Seal]')
    img_url = base_url + souf.attrs['src'].replace('..', '')
    print(img_url)

    filename = img_url.split("/")[-1]
    r = requests.get(img_url, stream = True)
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
        r.raw.decode_content = True
        
        # Open a local file with wb ( write binary ) permission.
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)
            moV = shutil.move(str(filename), output_dir)
    else:
        pass
getImg()