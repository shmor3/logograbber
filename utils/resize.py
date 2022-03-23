import os, glob, shutil
from PIL import Image
from dotenv import load_dotenv

def resize():
    load_dotenv()
    dst_dir = '../data/tmp/done'
    os.makedirs(dst_dir, exist_ok=True)
    files = glob.glob('../data/tmp/todo/*')
    for f in files:
        try:
            img = Image.open(f)
            print(img.size)
            img_resize = img.resize((150, 150))
            root, ext = os.path.splitext(f)
            basename = os.path.basename(root)
            imgName = os.path.join(dst_dir, basename + os.environ['saveImgAs'])
            img_resize.save(imgName)
        except OSError as e:
            pass
resize()