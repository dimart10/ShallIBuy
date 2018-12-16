#!/usr/bin/python

import sys
import re
import csv

pesos = [10, 0.1, 0.1, 0.1, -1]

with open('auxName.csv') as csvName:
	with open('auxMedias.csv') as csvMedias:
		readerName = csv.reader(csvName)
		rowName = readerName.next() 
		readerMedias = csv.reader(csvMedias)
		rowMedias = readerMedias.next()

		notas = [1, 1, 1, 1, 1]
		for i in range(0, 5):
			notas[i] = (float(rowName[i+21]) / float(rowMedias[i])) - 1

 		for i in range(0, 5):
 			print (notas[i]*pesos[i])
 		for i in range(0,6):
 			print (rowName[i+26])
