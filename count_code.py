#!/usr/bin/python
# coding:utf-8

"""
第 0007 题：有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
"""
import os


# 遍历文件夹和子文件夹
def walk_dir(filename):
    filepath = []
    for root, dirs, files in os.walk(filename):
        for f in files:
            if f.lower().endswith('.py'):
                filepath.append(os.path.join(root, f))
    return filepath


def count_code(path):
    file_name = os.path.basename(path)
    line_num = 0
    note_num = 0
    empty_line_num = 0
    note_flag = False
    # 注意注释可以是#，也可以时开头写的""" ... """这种形式，因此设置"""..."""的标志位
    with open(path, 'r') as f:
        # 利用read读取，同时按照\n来分割每行并返回
        for line in f.read().split('\n'):
            line_num += 1
            # """开始
            if line.strip().startswith('\"\"\"') and not note_flag:
                note_flag = True
                note_num += 1
                continue
            # """结束
            if line.strip().startswith('\"\"\"'):
                note_flag = False
                note_num += 1

            if line.strip().startswith('#') or note_flag:
                note_num += 1

            if len(line.strip()) == 0:
                empty_line_num += 1

    print '在%s中，一共有%s行代码，其中空行有%s行，注释行有%s行' % (file_name, line_num, empty_line_num, note_num)


if __name__ == "__main__":
    for f in walk_dir('.'):
        count_code(f)
