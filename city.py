#!/usr/bin/python
# coding=utf-8

"""
纯文本文件 city.txt为城市信息, 里面的内容（包括花括号）如下所示：

{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
"""

import xlwt
import json


def readtxt(filepath):
    with open(filepath, 'r') as f:
        text = f.read()
        text_json = json.loads(text)
    return text_json


def save_excal(content_dict, excal_name='city.xls'):
    wb = xlwt.Workbook()
    ws = wb.add_sheet("city", True)
    row = 0
    col = 0
    for x in range(len(content_dict)):
        ws.write(row, col, x + 1)
        col += 1
        ws.write(row, col, content_dict[str(x + 1)])
        col = 0
        row += 1
    wb.save(excal_name)

if __name__ == "__main__":
    save_excal(readtxt('city.txt'))
