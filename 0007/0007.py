#! usr/bin/env python3
# coding = utf-8


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
    dictcnt = {'sum':sum_cnt,'note':note_cnt,'blank':blank_cnt,'code':code_cnt}
    return dictcnt


def get_recursive_file(path):
    current_files = os.listdir(path)
    files = []
    for file in current_files:
        full_file = os.path.join(path,file)
        files.append(full_file)
        if os.path.isdir(full_file):
            next_level_files = get_recursive_file(full_file)
            files.extend(next_level_files)
    return files

if __name__ == "__main__":
    sum_cnt = 0
    note_cnt = 0
    blank_cnt = 0
    code_cnt = 0
    for file in get_recursive_file('.'):

        if file.endswith('.py'):
            count_code(file)
            sum_cnt += count_code(file)['sum']
            note_cnt += count_code(file)['note']
            blank_cnt += count_code(file)['blank']
            code_cnt += count_code(file)['code']
            print("{0}有{1}行,其中{2}行代码，{3}行注释，{4}行空白行".format(
                file,
                count_code(file)['sum'],
                count_code(file)['code'],
                count_code(file)['note'],
                count_code(file)['blank']))
    print("当前目录有{0}行,其中{1}行代码，{2}行注释，{3}行空白行".format(sum_cnt,code_cnt,note_cnt,blank_cnt))
