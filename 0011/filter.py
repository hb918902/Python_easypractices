#! /usr/bin/env python3
# coding = utf-8

import re
import os


def filter_word(a):
    flag = 0
    with open('filtered_word.txt', encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip(os.linesep)
            if re.search(line, a):
                flag += 1
    if flag:
        print('Freedom')
    else:
        print('Human Rights')


if __name__ == '__main__':
    str1 = input("Input some words: ")
    filter_word(str1)



