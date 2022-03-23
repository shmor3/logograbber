import os
import glob
from PIL import Image

def resize():
    dst_dir = 'data/tmp/done'
    os.makedirs(dst_dir, exist_ok=True)

    files = glob.glob('./data/tmp/todo/*')
    for f in files:
        try:
            img = Image.open(f)
            print(img.size)
            img_resize = img.resize((150, 150))
            root, ext = os.path.splitext(f)
            basename = os.path.basename(root)
            img_resize.save(os.path.join(dst_dir, basename + '.png'))
        except OSError as e:
            pass