#!/usr/bin/python
# -*-coding:utf-8-*-
import string
import random
import sys
KEY_LEN=20
KEY_ALL=200

def base_str():
	return string.digits+string.letters
# string.digits 和string.letters代表的是0-9和a-zA-Z

def key_gen():
	keylist=[random.choice(base_str()) for i in range(KEY_LEN)]
	return ("".join(keylist))#将链表当中的字符连接起来并以字符串返回

def key_num(num,result=None):
	if result is None:
		result=[]
	for i in range(num):
		result.append(key_gen())
	return result

def print_key(num):
	for i in key_num(num):
		print i

if __name__ =="__main__":
	print_key(KEY_ALL)
