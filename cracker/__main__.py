from utils import *
import numpy as np

a = np.zeros((30,30))
a[:, :15] = 20

save_img(a, "test")