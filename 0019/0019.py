#! /usr/bin/python3
# -*-coding:utf-8-*-

import xlrd
from xml.dom import minidom


def open_xls():
    excel = xlrd.open_workbook("numbers.xls")
    num_sheet = excel.sheet_by_index(0)
    sheet_content = []
    for row in range(num_sheet.nrows):
        print(sheet_content)
        row_value = num_sheet.row_values(row)
        # print(row_value)
        sheet_content.append(list(map(int,row_value)))
    return sheet_content


def build_xml(content):
    # Create Dom Object
    doc = minidom.Document()
    # Create root tag
    root = doc.createElement('root')
    doc.appendChild(root)
    # Create 'nums' tag
    nums = doc.createElement('numbers')
    root.appendChild(nums)
    # Create comment element
    nums.appendChild(doc.createComment("数字信息"))
    # Create text element
    nums.appendChild(doc.createTextNode(str(content)))

    # Save the xml file
    num_xml = open('num.xml', 'w')
    num_xml.write(doc.toprettyxml())
    num_xml.close()

if __name__ == '__main__':
    _content = open_xls()
    print(_content)
    build_xml(_content)
