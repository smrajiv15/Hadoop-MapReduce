#!/usr/bin/env python

import sys
import json

global_report = {}
max_crime = 0
crime_place = " "

def update_global_report(place, crime_dict):
	exist_cdict = global_report[place]

	for ckey in crime_dict:
		if ckey in exist_cdict.keys():
			exist_cdict[ckey] += crime_dict[ckey]
		else:
			exist_cdict[ckey] = crime_dict[ckey]

		exist_cdict["count"] += crime_dict[ckey]
		
	

for line in sys.stdin:
	ll = line.strip().split('\t')

	place      = ll[0]
	crime_str  = ll[1].replace("\'", "\"")
	crime_dict = json.loads(crime_str) 

	if place in global_report.keys():#if the place is there is the global report
		update_global_report(place, crime_dict)
	else:#new place
		global_report[place] = {}
		global_report[place]["count"] = 0
		update_global_report(place, crime_dict)
	
	cur_count = global_report[place]["count"] 
	if(max_crime < cur_count):
		max_crime = cur_count
		crime_place = place


print
print "STREET IN AUSTIN WITH MOST CRIMES: \"{}\" with {} crimes".format(crime_place, max_crime)
print
print "List of Crimes in that place:"
print("*"*29)


for key in global_report[crime_place]:
	print"{}".format(key)



