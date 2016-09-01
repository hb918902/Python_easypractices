#! /usr/bin/python3
# coding = utf-8

from html.parser import HTMLParser
import re

class TextHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.nohandletags = ["script","style"]  #
        self.processing = None

    def handle_starttag(self, tag, attrs):
        if tag in self.nohandletags:
            self.processing = tag

    def handle_data(self, data):
        if not self.processing and not re.match('^$',data):
            print(data)

    def handle_endtag(self, tag):
        if tag == self.processing:
            self.processing = None

if __name__ == '__main__':
    parser = TextHTMLParser()
    with open("test.html") as f:
        for line in f:
            parser.feed(line)
        parser.close()


