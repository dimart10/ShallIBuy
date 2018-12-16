#!/usr/bin/python

import sys
import re
import csv

scoreSum = 0
scoreTotal = 0.0
recomSum = 0
recomTotal = 0.0
ownerSum = 0
ownerTotal = 0.0
playerSum = 0
playerTotal = 0.0
priceSum = 0
priceTotal = 0.0

next(sys.stdin)

for line in sys.stdin:
	values = line.split(" ")
	score = values[0]
	recom = values[1]
	owner = values[2]
	player = values[3]
	price = values[4]

	if score != '0':
		scoreSum += 1
		scoreTotal = scoreTotal + float(score) 
	if recom != '0':
		recomSum += 1
		recomTotal = recomTotal + float(recom) 
	if owner != '0':
		ownerSum += 1
		ownerTotal = ownerTotal + float(owner) 
	if player != '0':
		playerSum += 1
		playerTotal = playerTotal + float(player) 
	if price != '0.0':
		priceSum += 1
		priceTotal = priceTotal + float(price) 
	

with open('auxMedias.csv', 'wb') as csvfile:
	salidaCSV = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	salidaCSV.writerow([scoreTotal/scoreSum, recomTotal/recomSum, ownerTotal/ownerSum, playerTotal/playerSum, priceTotal/priceSum])
