from utils import *

from PIL import Image, ImageDraw, ImageFont
from random import uniform, randint
import numpy as np

def bring_to_corner(img):
	a = np.asarray(img).copy()
	mnv, mnh = np.argmax(a, axis=0), np.argmax(a, axis=1)
	y, x = np.min(mnv[mnv>0]), np.min(mnh[mnh>0])
	
	a = np.roll(a, -y, axis=0)
	a = np.roll(a, -x, axis=1)
	return Image.fromarray(a[:35, :35])

def random_resize(img):
	x = randint(25, 30)
	img = img.resize((x, x))

	a = np.asarray(img).copy()
	a = np.concatenate((a, np.zeros((x, 30-x), dtype=a.dtype)), axis=1)
	a.resize((30, 30))

	a = np.roll(a, randint(0, 5), axis=0)
	a = np.roll(a, randint(0, 5), axis=1)
	return Image.fromarray(a)

def make_digit(d):
	size = (70, 70)

	img = Image.new("1", size)
	draw = ImageDraw.Draw(img)
	font = ImageFont.truetype("data/arial.ttf", 30)

	draw.text((15, 10), str(d), fill=255, font=font)

	coeffs = (
		uniform(0, 15), uniform(0, 15), uniform(0, 15), uniform(55, 70),
		uniform(55, 70), uniform(55, 70), uniform(55, 70), uniform(0, 15)
	)

	img = img.transform(size, Image.QUAD, coeffs)
	img = bring_to_corner(img)
	img = random_resize(img)

	# img.save(f"tests/{name}.png")
	return np.asarray(img).copy().flatten()

@timed_func
def generate_dataset(n):
	data, label = [], []
	for d in range(10):
		print(f"generating for {d}...")
		for i in range(n):
			data.append(make_digit(d))
			label.append(d)
	return data, label

