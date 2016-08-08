#!/usr/bin/python
# coding=utf-8

"""
 纯文本文件 numbers.txt, 里面的内容（包括方括号）如下所示：

[
    [1, 82, 65535],
    [20, 90, 13],
    [26, 809, 1024]
]
"""

import json
import xlwt


def readtxt(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
        text_json = json.loads(text)
    return text_json


def save_excal(content_dict, excal_name='numbers.xls'):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("numbers", True)
    row = 0
    col = 0
    for i in range(len(content_dict)):
        for j in range(len(content_dict[i])):
            ws.write(row, col, content_dict[i][j])
            col += 1
        row += 1
        col = 0
    wb.save(excal_name)


if __name__ == "__main__":
    save_excal(readtxt('numbers.txt'))
