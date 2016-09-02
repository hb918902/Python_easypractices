#! /usr/bin/python3
# -*-coding:utf-8-*-

import xlrd
from xml.dom import minidom
import re

def open_xls():
    excel = xlrd.open_workbook("city.xls")
    city_sheet = excel.sheet_by_index(0)
    sheet_content = {}
    for row in range(city_sheet.nrows):
        row_value = city_sheet.row_values(row)
        # print(row_value)
        for i in range(len(row_value)):
            if type(row_value[i]) == float:
                row_value[i] = int(row_value[i])
        sheet_content[str(row+1)] = row_value[1:]
    return sheet_content


def build_xml(content):
    # Create Dom Object
    doc = minidom.Document()
    # Create root tag
    root = doc.createElement('root')
    doc.appendChild(root)
    # Create 'citys' tag
    citys = doc.createElement('citys')
    root.appendChild(citys)
    # Create comment element
    citys.appendChild(doc.createComment("城市信息"))
    # Create text element
    citys.appendChild(doc.createTextNode(\
        re.sub('\[|\]','',str(content))))

    # Save the xml file
    city_xml = open('city.xml', 'w')
    city_xml.write(doc.toprettyxml())
    city_xml.close()

if __name__ == '__main__':
    _content = open_xls()
    build_xml(_content)
