#!/usr/bin/python
# coding=utf-8

"""
第 0020 题： 登陆中国联通网上营业厅 后选择「自助服务」 --> 「详单查询」，然后选择你要查询的时间段，
点击「查询」按钮，查询结果页面的最下方，点击「导出」，就会生成类似于 2014年10月01日～2014年10月31日
通话详单.xls 文件。写代码，对每月通话时间做个统计。
"""

import xlrd

Sum = 0


def readexl(filename):
    global Sum
    excal = xlrd.open_workbook(filename)
    excal_sheet = excal.sheet_by_index(0)
    nrow = excal_sheet.nrows
    for i in range(6, nrow):
        time = str(excal_sheet.row_values(i)[4])
        hour = int(time[:2])
        minute = int(time[3:5])
        second = int(time[6:])
        Sum += hour * 60 * 60 + minute * 60 + second
    return Sum


if __name__ == "__main__":
    print '通话的总时长为%ss' % readexl('18800205686_通话详单.xls')
