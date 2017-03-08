#!/usr/bin/env python

import sys

global_report = {}

for line in sys.stdin:
	wl = line.strip(',').split(',')
	place = wl[5]
	crime = wl[1]

	if place in global_report.keys():
		pl_crime_dict = global_report[place]#if place found, get the crime dict

		if crime in pl_crime_dict.keys(): #if crime is found in the dict make +1
			pl_crime_dict[crime] += 1
		else: # else create the key and initialize
			pl_crime_dict[crime] = 1
			
	else: #if place is not found
		global_report[place] = {} #create an empty dictionary
		global_report[place][crime] = 1 #enter the new key(crime) with value initialized


for key in global_report:
	print"{}\t{}".format(key, global_report[key])
