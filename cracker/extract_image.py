from utils import *

from PIL import Image
import os, io, base64

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

js_script = """
let img = document.getElementsByClassName("loginCaptcha")[0].children[0];
let canvas = document.createElement("canvas");
canvas.height = img.height; canvas.width = img.width;

let context = canvas.getContext("2d");
context.drawImage(img, 0, 0, img.width, img.height)
return canvas.toDataURL();
"""

@timed_func
def load_captcha(erp="https://student.robcol.k12.tr/"):
	print("Starting driver...")
	options = Options()
	options.headless = True
	driver = webdriver.Firefox(
		options=options,
		service_log_path=os.path.devnull
	)
	
	print("Loading ERP...")
	driver.get(erp)

	print("Getting image...")
	data = driver.execute_script(js_script).split(",")[1]
	driver.quit()
	
	img = Image.open(io.BytesIO(base64.b64decode(data)))
	return img