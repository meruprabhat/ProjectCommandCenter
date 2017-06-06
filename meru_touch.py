#!/usr/bin/python

import sys,os
#Getting all arguments as file name except first argument
a=sys.argv[1:]
#Looping through all the file names
for i in a:
	#Check Whether the file with same file already exists, if yes through an exception
	try:
		a=open(i,'r')
		#If file is there no need to create new or update the data
		if (a is True):
		pass
	#If the file with same filename do ot exists create the file
	except:
		f=open(i,"w+")
		

