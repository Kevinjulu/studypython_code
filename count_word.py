#!/usr/bin/python
#-*-coding:utf8-*-
#任一个英文的纯文本文件，统计其中的单词出现的个数。

import re

def count_num(filename):
	fo=open(filename,'rb')
	s=fo.read()
	words=re.findall(r'[a-zA-Z]+',s)
#这里使用了原始字符串，+表示前面的为1个或者多个匹配项
	return len(words)


if __name__=='__main__':
	num=count_num('/root/pythondir/count_test.txt')
	print '单词的个数为：'+str(num)
