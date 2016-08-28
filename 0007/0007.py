#! usr/bin/env python3
# coding = utf-8

"""仅适用于当前目录中的py文件，多层目录无法计算"""

import os
import re


def count_code(filename):
    note = re.compile("^#")
    blank = re.compile("^$")
    sum_cnt = 0
    note_cnt = 0
    blank_cnt = 0
    code_cnt = 0
    with open(filename) as f:
        for line in f:
            if re.search(note,line):
                note_cnt += 1
            elif re.search(blank,line):
                blank_cnt += 1
            else:
                code_cnt += 1
            sum_cnt += 1
    print("{0} 有{1}行，其中{2}代码，{3}行注释，{4}行空白行。".format(filename,sum_cnt,code_cnt,note_cnt,blank_cnt))

def get_dir(path):
    files = os.listdir(path)
    for file in files:
        if file.endswith('.py'):
            count_code(file)

if __name__ == "__main__":
    get_dir('.')












