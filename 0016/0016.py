#! /usr/bin/python3
# -*-coding:utf-8-*-


import xlwt,json


file = xlwt.Workbook(encoding='utf-8')
table = file.add_sheet('numbers',cell_overwrite_ok=True)
with open('numbers.txt') as f:
    txt = f.read()
json_txt = json.loads(txt)
for x in range(len(json_txt)):
    for y in range(len(json_txt[x])):
        table.write(x,y,json_txt[x][y])

file.save('city.xls')



