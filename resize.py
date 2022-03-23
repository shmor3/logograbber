import os
import glob
from PIL import Image

dst_dir = 'data/done'
os.makedirs(dst_dir, exist_ok=True)

files = glob.glob('./data/todo/*')
for f in files:
    try:
        img = Image.open(f)
        print(img.size)
        img_resize = img.resize((150, 150))
        root, ext = os.path.splitext(f)
        basename = os.path.basename(root)
        img_resize.save(os.path.join(dst_dir, basename + '.png'))
        print(img_resize.size)
    except OSError as e:
        pass