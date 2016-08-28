#! /usr/bin/env python
# coding = utf-8

from PIL import Image, ImageDraw, ImageFont
import random

headnum = str(random.randint(1, 99))

# read image
im = Image.open('a.jpg')
w, h = im.size
wDraw = 0.08*w
hDraw = 0.08*w

# draw image
font = ImageFont.truetype('/usr/share/fonts/truetype/droid/DroidSans.ttf', 30)
draw = ImageDraw.Draw(im)
draw.text((wDraw,hDraw), headnum, font=font, fill=(255,100,330))

# Save image
im.save('b.png', 'png')


