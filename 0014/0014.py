#! /usr/bin/python3
# -*-coding:utf-8-*-

import xlwt
import json
from collections import OrderedDict

wb = xlwt.Workbook(encoding='utf-8')
sheet1 = wb.add_sheet('student',cell_overwrite_ok=True)

with open('student.txt') as f:
    txt = f.read()
json_txt = json.loads(txt,object_pairs_hook=OrderedDict)  # 保持txt中的顺序
print(json_txt)
rowcnt = 0
for k in json_txt.keys():
    sheet1.write(rowcnt,0,k)
    for j in range(len(json_txt[k])):
        sheet1.write(rowcnt,j+1,json_txt[k][j])
    rowcnt += 1

wb.save('student.xls')
