#!/usr/bin/python
# coding=utf-8

"""
第 0014 题： 纯文本文件 student.txt为学生信息, 里面的内容（包括花括号）如下所示,
请将上述内容写到 student.xls 文件中
{
    "1":["张三",150,120,100],
    "2":["李四",90,99,95],
    "3":["王五",60,66,68]
}
"""

import json
import xlwt



def readtxt(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
        text_json = json.loads(text)
    return text_json


def save_excal(content_dict, excal_name='student.xls'):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("student", True)
    row = 0
    col = 0
    for i in content_dict.keys():
        ws.write(row, col, i)
        for j in content_dict[i]:
            col += 1
            ws.write(row, col, j)
        row += 1
        col = 0
    wb.save(excal_name)


if __name__ == "__main__":
    save_excal(readtxt('student.txt'))
