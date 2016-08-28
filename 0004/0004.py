#! /usr/bin/env python3
# coding = utf-8

from collections import Counter
import os

def count_alp(filename=None,str1=None):
    sumstr1 = 0
    if not os.path.isfile(filename):
        print('There is no',filename,'.')
    else:
        with open(filename) as f:
            for line in f:
                num = Counter(line)
                sumstr1 += num[str1]
        print(filename,'有',sumstr1,'个',str1,'字符。')

count_alp('Eng.txt',"a")





