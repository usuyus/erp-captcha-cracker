# ERP Captcha Cracker
An in-progress attempt to solve the annoying captcha in https://student.robcol.k12.tr/.

The """cracker""" has several stages:
- Image Extraction: Gets the exact captcha image from the site via a JS script and returns it as a data URI.
- Digit Extraction: Sanitizes the image by removing random stuff and extracts the digits as a 30x30 binary matrix
- Digit Recognition: Uses a pre-trained model to classify each digit.

I plan to make this a full-on extension, but first, I have to make it work :/

Note: just run "python3 cracker" in the project directory to make the program load a random captcha from ERP and attempt to solve it (and miserably fail at it...)
