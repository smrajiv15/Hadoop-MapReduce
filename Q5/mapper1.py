#!/usr/bin/env python

import sys
import re

patt = re.compile(r"\d{1,2}[/]\d{1,2}[/]\d{1,4}")

global_report = {}

def parse_date(date):
	dl = date.strip().split("/")
	return int(dl[0]) - 1

for line in sys.stdin:
	wl = line.strip(',').split(',')
	crime = wl[1]
	date = wl[2]
	mon_index = 0

	if patt.search(date):
		if crime in global_report.keys():
			mon_index = parse_date(date)
			global_report[crime][mon_index] += 1
		else:
			global_report[crime] = [0]*12
			mon_index = parse_date(date)
			global_report[crime][mon_index] = 1
	else:
		continue	


for key in global_report:
	print"{}\t{}".format(key, global_report[key])
