#! /usr/bin/python3
# -*-coding:utf-8-*-

import xlrd
from xml.dom import minidom


def open_xls():
    excel = xlrd.open_workbook("student.xls")
    student_sheet = excel.sheet_by_name("student")
    sheet_content = {}
    for row in range(student_sheet.nrows):
        row_value = student_sheet.row_values(row)
        print(row_value)
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
    # Create 'students' tag
    students = doc.createElement('students')
    root.appendChild(students)
    # Create comment element
    students.appendChild(doc.createComment("学生信息表\"id\" : [名字, 数学, 语文, 英文]"))
    # Create text element
    students.appendChild(doc.createTextNode(str(content)))

    # Save the xml file
    student_xml = open('student.xml', 'w')
    student_xml.write(doc.toprettyxml())
    student_xml.close()

if __name__ == '__main__':
    _content = open_xls()
    print(_content)
    build_xml(_content)
