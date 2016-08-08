#!/usr/bin/python
#-*-coding:utf8-*-

#第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。
from PIL import Image, ImageDraw, ImageFont
import os 

iPhone5_Width=640
iPhone5_Height=1136
filemode=('jpg','jpeg')
def changesize(filename,file_new_name,width=iPhone5_Width,height=iPhone5_Height):
	im=Image.open(filename)
	w,h=im.size
	
	if w>width:
		h=h*w/width
		w=width
		
	if h>height:
		w=w*h/height
		h=height
		
	im_resized=im.resize((w,h),Image.ANTIALIAS)
	im_resized.save(file_new_name)
	
def walk_dir(path):
	for root,dirs,files in os.walk(path):
		for file in files:
			if file.lower().endswith(filemode):
				path_dst=os.path.join(root,file)
				#连接root和file名，中间自动加入/
				f_n_name='iPhone5'+path_dst
				changesize(path_dst,f_n_name)
				
				
				
if __name__=="__main__":
	walk_dir('/root/pythondir/pic')
	
