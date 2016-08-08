#!/usr/bin/python
# coding=utf-8

"""
 将 第 0015 题中的 city.xls 文件中的内容写到 city.xml 文件中，如下所示：

<?xmlversion="1.0" encoding="UTF-8"?>
<root>
<citys>
<!--
    城市信息
-->
{
    "1" : "上海",
    "2" : "北京",
    "3" : "成都"
}
</citys>
</root>
"""

import json
import xlrd
from lxml import etree


def read_xls(file_name):
    exl = xlrd.open_workbook(file_name)
    exl_sheet = exl.sheet_by_name('city')
    # data是一个字典
    data = {}
    for i in range(exl_sheet.nrows):
        data[exl_sheet.row_values(i)[0]] = exl_sheet.row_values(i)[1:]
    return json.dumps(data, encoding='utf-8', ensure_ascii=False)


def save_to_xml(data, newfilename):
    root = etree.Element('root')
    citys = etree.SubElement(root, 'citys')
    citys.append(etree.Comment(u'城市信息'))
    citys.text = data

    student_xml = etree.ElementTree(root)
    student_xml.write(newfilename, pretty_print=True, xml_declaration=True, encoding='utf-8')


if __name__ == "__main__":
    content = read_xls('city.xls')
    save_to_xml(content, 'city.xml')
