#!/usr/bin/python

import sys
import re
import csv

with open('auxParecidos.csv') as csvfile:

	reader = csv.reader(csvfile)
	reader.next()

	for row in reader:
		 for i in range(0, 5):
		 	print row[i],
		 print "\n",
