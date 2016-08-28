#! /usr/bin/env python3
# coding = utf-8

import os,re

def count_alp(filename=None,str1=None):
    sumstr1 = 0
    r1 = re.compile(str1)
    if not os.path.isfile(filename):
        print('There is no',filename,'.')
    else:
        with open(filename) as f:
            for line in f:
                num = len(re.findall(r1,line))
                sumstr1 += num
        print(filename,'有',sumstr1,'个',str1,'字符。')

if __name__ == "__main__":
    filelist = os.listdir(os.getcwd())
    for file in filelist:
        if os.path.isfile(file):
            count_alp(file,"Python")


