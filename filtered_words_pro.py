#!/usr/bin/python
# coding=utf-8

"""
敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，
例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
"""



def trans_to_words():
    word = raw_input('>')
    word = word.decode('utf-8')
    word_temp = word
    judge_flag = False
    with open('filtered_words.txt', 'r') as f:
        text = f.read().decode('utf-8')
    for i in text.strip().split('\n'):
        if i in word:
            word_temp = word_temp.replace(i, '*' * len(i))
            judge_flag = True
    if judge_flag:
        print word_temp
    else:
        print word


if __name__ == "__main__":
    trans_to_words()