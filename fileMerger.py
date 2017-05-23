#!/usr/bin/python
a={}
import csv
import sys
files = sys.argv[1:]
for file  in files:
	r = open(file,"r")
	csvFile = csv.reader(r)
	for row in csvFile:
		key = row[0]
		if(a.has_key(key)):
			a[key] = a[key] + row[1:]
		else:
			a[key] = row[1:]
res = open("/Users/pramodvadiraj/Desktop/result.csv","w")
writeToFile = csv.writer(res)
for k,v in a.items():
	v.insert(0,k)
	writeToFile.writerow(v)
print "done"



