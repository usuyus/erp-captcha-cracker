from utils import *
from extract_image import load_captcha
from extract_digits import get_digits
from train_model import train_new_model, predict_captcha

from PIL import Image

def main(new_img=True):
	if new_img: img = load_captcha()
	else: load_img("captcha")

	ds = get_digits(img)
	print(predict_captcha(ds))


main()