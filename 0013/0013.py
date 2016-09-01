#! /usr/bin/python3
# -*-coding:utf-8-*-

from html.parser import HTMLParser
import urllib.request


class ImgParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.links = []   # 保存图片链接地址

    def handle_starttag(self, tag, attrs):
        if tag == "img" and ('class','BDE_Image') in attrs:
            for i in range(len(attrs)):
                if attrs[i][0] == "src":
                    self.links.append(attrs[i][1])


if __name__ == "__main__":
    Imgs = ImgParser()
    url = "http://tieba.baidu.com/p/2166231880"
    with urllib.request.urlopen(url) as f:
        Imgs.feed(f.read().decode('utf-8'))
        for i in range(len(Imgs.links)):
            print("第",i,"张图片")
            urllib.request.urlretrieve(Imgs.links[i],str(i)+".jpg")







