import utils.resize as resize
import utils.getImg as getImg
import utils.browser as browser
from dotenv import load_dotenv

def __main__():
    load_dotenv()

    getImg()
    resize()