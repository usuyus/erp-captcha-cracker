from utils import *
from extract_image import load_captcha
from extract_digits import get_digits
from test_data import generate_dataset

from PIL import Image

# img = load_captcha()

imgs, labels = generate_dataset(1)

for i, img in zip(range(len(imgs)), imgs):
	save_img(img.reshape((30,30)), f"{i}")