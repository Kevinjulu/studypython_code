#!/usr/bin/python
# coding=utf-8

"""
第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，
否则打印出 Human Rights。
"""


def trans_to_words():
    word = raw_input('>')
    judge_flag = False
    with open('filtered_words.txt', 'r') as f:
        text = f.read()
    for i in text.strip().split('\n'):
        if i in word:
            judge_flag = True
    if judge_flag:
        print 'Freedom'
    else:
        print 'Human Rights'


if __name__ == "__main__":
    trans_to_words()