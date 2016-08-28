#! /usr/bin/env python3
# coding = utf-8

import re
import os


def filter_word(a):
    with open('filtered_word.txt',encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip(os.linesep)
            a = re.sub(line, len(line)*'*', a)
        print(a)

if __name__ == '__main__':
    str1 = input("Input some words: ")
    filter_word(str1)



