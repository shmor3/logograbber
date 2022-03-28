import time, os, requests, shutil, glob, re
from dotenv import load_dotenv
from bs4 import BeautifulSoup
from PIL import Image
import pandas as pda

load_dotenv()


class getImg():
    def imgDl():
        site = 'http://10.0.0.123/images/u/us-co.dv).gif'

        response = requests.get(site)

        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        urls = [img['src'] for img in img_tags]


        for url in urls:
            filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
            if not filename:
                print("Regex didn't match with the url: {}".format(url))
                continue
            with open(filename.group(1), 'wb') as f:
                if 'http' not in url:
                    url = '{}{}'.format(site, url)
                response = requests.get(url)
                f.write(response.content)

class resize():
    def webImg():
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

class cleanUp():
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


getImg()
resize()
cleanUp()