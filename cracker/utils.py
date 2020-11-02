import time, os
import numpy as np
from PIL import Image

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
	if not os.path.exists("../imgs"):
		os.mkdir("../imgs")

	if type(a) == np.ndarray:
		x = np.floor(a / np.max(a) * 255).astype(np.uint8)
		Image.fromarray(x).save(f"../imgs/{name}.png")
	else:
		a.save(f"../imgs/{name}.png")

def load_img(name):
	pass