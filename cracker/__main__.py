from utils import *
from extract_image import load_captcha

from PIL import Image

img = load_captcha()
print(type(img) == Image)
save_img(img, "test")
