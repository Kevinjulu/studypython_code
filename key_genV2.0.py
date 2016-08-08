#!/usr/bin/python
# -*-coding:utf-8 -*-
# 第 0001 题：做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），
# 使用 Python 如何生成 200 个激活码（或者优惠券）？
import random
import string


key_len = int(raw_input("请输入优惠码的长度："))
key_all = int(raw_input("请输入优惠码的个数："))


def base_str():
    return string.letters + string.digits


def print_num(num1, num2, record=None):
    if record is None:
        record = []
    for i in range(num1):
        key_list = [random.choice(base_str()) for j in range(num2)]
        record.append("".join(key_list))
    return record


if __name__ == "__main__":
    fo = open("/root/pythondir/YHM.txt", "w+")
    a = print_num(key_all, key_len)
    for i in range(key_all):
        fo.write(a[i] + '\n')
    fo.close()
    print "写入成功！"
