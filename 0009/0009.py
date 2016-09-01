#! /usr/bin/python3
# coding = utf-8

from html.parser import HTMLParser


class TextHTMLParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.hrefs = []

    def handle_starttag(self, tag, attrs):
        for i in range(len(attrs)):
            if 'href' == attrs[i][0]:
                self.hrefs.append(attrs[i][1:])


if __name__ == '__main__':
    parser = TextHTMLParser()
    with open("test.html") as f:
        for line in f:
            parser.feed(line)
        parser.close()
    print(parser.hrefs)


