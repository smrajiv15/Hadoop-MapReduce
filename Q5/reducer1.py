#!/usr/bin/env python

import sys
import json

global_report = {}

def add_with_list(mon_list, crime):
	cur_list = global_report[crime]
	
	for i, (ci,ni) in enumerate(zip(cur_list, mon_list)):
		cur_list[i] = ci + int(ni)


for line in sys.stdin:
	map_list = line.strip().split("\t")
	crime = ""
	mon_list = ""

	if len(map_list) == 2:
		crime    = map_list[0]
		mon_list = json.loads(map_list[1])

		if crime in global_report.keys():
			add_with_list(mon_list, crime)
		else:
			global_report[crime] = [0]*12
			add_with_list(mon_list, crime)
	else:#None Type
		mon_list = json.loads(map_list[0])

		if "None" in global_report.keys():
			add_with_list(mon_list, "None")
		else:
			global_report["None"] = [0]*12
			add_with_list(mon_list, "None")


for key in global_report:
	print"{}\t{}".format(key, global_report[key])



