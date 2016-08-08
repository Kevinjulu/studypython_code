#!usr/bin/python
#coding=utf-8

"""
第 0006 题：你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，
假设内容都是英文，请统计出你认为每篇日记最重要的词。
"""

import os
import re

#dirs=raw_input("请输入目录路径")

def walk_dir(path):
	file_path = []
	#分别是根目录   目录下的文件夹   目录下的文件,注意利用for循环会递归调用所有的文件夹
	for root, dirs, files in os.walk(path):
		for f in files:
			if f.lower().endswith('txt'):
				file_path.append(os.path.join(root,f))
	return file_path

def find_key_word(filepath):
	word_dir={}
	filename=os.path.basename(filepath)
	with open(filepath) as f:
		text=f.read()
		word_list=re.findall(r'[a-zA-Z]+',text.lower())
		for word in word_list:
			if word in word_dir:
				word_dir[word]+=1
			else:
				word_dir[word]=1
		#利用第二个关键字进行排序，key和cmp都可以接上匿名函数作为比较函数,返回的是一个list！！	
		word_sort_list=sorted(word_dir.items(),key=lambda d:d[1])
		print "在%s文件中，%s为关键词，出现的次数为%s次。" %(filename,word_sort_list[-1][0],word_sort_list[-1][1])

if __name__ =="__main__":
	for files in walk_dir(os.getcwd()):
	#for files in walk_path(dirs):
		find_key_word(files)
