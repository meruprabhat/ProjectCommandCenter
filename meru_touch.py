#!/usr/bin/python

import sys,os
a=sys.argv[1:]
print a
new=

for i in a:
	try:
		a=open(i,'r')
		if (a is True):
			os.utime(i,(new,new))
			pass
	except:
		f=open(i,"w+")
		

