#! /usr/bin/python
# -*-coding:utf-8-*-

from PIL import Image,ImageFont,ImageDraw,ImageFilter
import random


class ConfirmationChar(object):
    def __init__(self,num=4):
        self.num = num
        self._width = num*60
        self._height = 60

    # 随机字母A-Z
    def rndChar(self):
        return chr(random.randint(65,90))

    # 随机颜色1
    def rntColor(self):
        return (random.randint(64,255), random.randint(64,255),random.randint(64,255))

    # 随机颜色2

    def rntColor2(self):
        return (random.randint(32,127),random.randint(32,127),random.randint(32,127))

    def generate(self):
        image = Image.new('RGB',(self._width,self._height),(255,255,255))
        font = ImageFont.truetype('/usr/share/fonts/truetype/ubuntu-font-family/Ubuntu-B.ttf',36)
        draw = ImageDraw.Draw(image)
        # 填充像素
        for x in range(self._width):
            for y in range(self._height):
                draw.point((x,y),fill=self.rntColor())
        # 填充字符
        for t in range(self.num):
            draw.text((60*t +10,10),self.rndChar(),font=font,fill=self.rntColor2())
        # 模糊处理
        image = image.filter(ImageFilter.BLUR)
        image.save('1.jpg','jpeg')


if __name__ == '__main__':
    testhar = ConfirmationChar(5)
    testhar.generate()
