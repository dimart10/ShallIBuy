#!/usr/bin/python

import csv
import sys
import re

with open('games_features.csv') as csvfile:
    name = sys.argv[1]
    reader = csv.reader(csvfile)
    reader.next()
    found = False
    for row in reader:
        auxName = row[3]
        if(name == auxName):
            with open('auxName.csv', 'wb') as csvfile:
            	salidaCSV = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                salidaCSV.writerow([row[35], row[36], row[37], row[38], row[39], row[40], row[41], row[42], 
                	row[43], row[44], row[45], row[46], row[47], row[48], row[49], row[50], row[51], row[52], row[53], row[54], row[55], 
                	row[9], row[12], row[15], row[17], row[58], row[4], row[21], row[22], row[26], row[27], row[28]])
                found = True
                break
    if(found == False):
    	print 'Juego no encontrado.'
    else :
    	print 'Juego encontrado.'
