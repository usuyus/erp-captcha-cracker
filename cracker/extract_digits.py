from utils import *

from PIL import Image
import numpy as np
from scipy.ndimage.measurements import label

def get_digits(img, gray_thres=130, size_thres=20):
	a = np.asarray(img).copy()
	a = np.delete(a, 3, 2) # remove alpha channel

	mask = a[:, :, 0] >= gray_thres
	a[mask, :] = 255 # remove gridline + gray dots
	a[find_holes(mask)] = [25, 151, 87] # fill holes
	
	# turn into grayscale
	a = 255 - np.mean(a, axis=2) > 0

	save_img(a, "pre")

	# a = remove_spots(a, size_thres)
	lbl, cnt = label(a) # find connected components using scipy
	a = lbl

	digits = []

	for i in range(1, cnt+1):
		cur = a == i
		if np.sum(cur) < size_thres: a[cur] = 0
		else:
			mnv, mnh = np.argmax(cur, axis=0), np.argmax(cur, axis=1)
			y, x = np.min(mnv[mnv>0]), np.min(mnh[mnh>0])
			cur = np.roll(cur, -y, axis=0)
			cur = np.roll(cur, -x, axis=1)
			cur = cur[:30,:30]
			digits.append((x, cur))

	res = []
	for (x, d), i in zip(sorted(digits), range(6)):
		res.append(d.flatten())
		save_img(d, f"{i}")
	save_img(a>0, "result")

	return res

# super jank but works
def find_holes(mask):
	res = mask
	mask = ~mask

	mask = np.roll(mask, 1, axis=0)
	res = res & mask
	mask = np.roll(mask, -2, axis=0)
	res = res & mask
	mask = np.roll(mask, 1, axis=0)

	mask = np.roll(mask, 1, axis=1)
	res = res & mask
	mask = np.roll(mask, -2, axis=1)
	res = res & mask
	mask = np.roll(mask, 1, axis=1)

	return res

# not reliable enough - still leaves some spots - also jank
def remove_spots(a, threshold):
	# vertical distances
	zeros = a == 0
	idx = np.repeat(np.arange(a.shape[0])[:, np.newaxis], a.shape[1], axis=1)

	down = idx - np.maximum.accumulate(idx*zeros)
	down *= ~zeros

	zeros = zeros[::-1]
	up = idx - np.maximum.accumulate(idx*zeros)
	up = up[::-1] * ~zeros[::-1]

	# horizontal distances
	zeros = a == 0
	idx = np.repeat(np.arange(a.shape[1])[:, np.newaxis].T, a.shape[0], axis=0)

	right = idx - np.maximum.accumulate(idx*zeros, axis=1)
	right *= ~zeros

	zeros = zeros[:, ::-1]
	left = idx - np.maximum.accumulate(idx*zeros, axis=1)
	left = left[:, ::-1] * ~zeros[:, ::-1]

	return (up + down + left + right) >= threshold