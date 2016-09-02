#! /usr/bin/python3
# -*-coding:utf-8-*-


import xlwt,json
from collections import OrderedDict

file = xlwt.Workbook(encoding='utf-8')
table = file.add_sheet('city',cell_overwrite_ok=True)
with open('city.txt') as f:
    txt = f.read()
json_txt = json.loads(txt,object_pairs_hook=OrderedDict)
for x in range(len(json_txt)):
    table.write(x,0,x+1)
    table.write(x,1,json_txt[str(x+1)])
file.save('city.xls')



