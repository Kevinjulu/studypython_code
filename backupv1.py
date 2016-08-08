#!/usr/bin/python

import os
import time

source=['/root/shell']

target_dir='/root/'

today=target_dir+time.strftime("%Y%m%d")

now=time.strftime('%H%M%S')

comment=raw_input('Enter a comment--->')

if len(comment)==0:
	target=today+os.sep+now+'.zip'
else:
	target=today+os.sep+now+'_'+comment.replace(' ','_')+'.zip'

if not os.path.exists(today):
	os.mkdir(today)
	print 'successfully created dir!'

zip_command="zip -qr '%s' %s" % (target,' '.join(source))

if os.system(zip_command)==0:
	print 'successful backup'+target
else:
	print 'back failed'
