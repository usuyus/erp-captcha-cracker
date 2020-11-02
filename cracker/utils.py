import time, os
import numpy as np
from PIL import Image
from PIL.PngImagePlugin import PngImageFile

def timed_func(func):
	def wrap(*args, **kwargs):
		print(f"=> {func.__name__} begin")
		begin = time.time()
		res = func(*args, **kwargs)
		end = time.time()
		print(f"=> {func.__name__} end [{end - begin:.4f}s]")
		return res
	return wrap

def save_img(a, name):
	if not os.path.exists("imgs"):
		os.mkdir("imgs")

	if type(a) == np.ndarray:
		x = np.floor(a / np.max(a) * 255).astype(np.uint8)
		Image.fromarray(x).save(f"imgs/{name}.png")
	elif type(a) == PngImageFile:
		a.save(f"imgs/{name}.png")
	else:
		print(f"warning: not supported image \"{name}\"")

def load_img(name):
	try:
		return Image.open(f"imgs/{name}.png")
	except FileNotFoundError as e:
		print(f"warning: couldn't find image \"{name}\"")
