import os, glob, shutil
from PIL import Image
from dotenv import load_dotenv

class resize():
    def webImg():
        load_dotenv()
        dst_dir = str(os.environ['done'])
        dl_Dir = str(os.environ['dl_Dir'])
        os.makedirs(dst_dir, exist_ok=True)
        os.makedirs(dl_Dir, exist_ok=True)

        files = glob.glob(str(os.environ['DL_Dir'] + '/*'))
        for f in files:
            try:
                img = Image.open(f)
                img_resize = img.resize((int(os.environ['width']), int(os.environ['height'])))
                root, ext = os.path.splitext(f)
                basename = os.path.basename(root)
                imgName = os.path.join(dst_dir, basename + os.environ['saveImgAs'])
                img_resize.save(imgName)
                print(u'\u001b[32mResize Successful\n')
            except OSError as e:
                pass
    def cleanUp():
        folder = os.environ['DL_Dir']
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
                print('\u001b[32mCleanup Successful\n')    
            except Exception as e:
                print(u'\u001b[31mCleanup Failed\n')
                pass
    webImg()
    cleanUp()
resize()