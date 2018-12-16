#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import re

categorias = []
generos = []
with open('auxNameCSV.csv') as csvfile:
    readerName = csv.reader(csvfile)
    for row in readerName:
        for i in range(0, 8):
            categorias.append(row[i])
        for i in range(8, 21):
            generos.append(row[i])
    with open('auxSimilarCSV.csv', 'wb') as csvfile:
        salidaCSV = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        salidaCSV.writerow(generos)
with open('games_features.csv') as csvfile:
    reader = csv.reader(csvfile)
    numFilas = 0
    with open('auxSimilarCSV.csv', 'wb') as csvfile:
        salidaCSV = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            ++numFilas
            genFound = 0
            catFound = 0
            for i in range(0, 8):
                if(categorias[i] == 'true' and categorias[i] == row[i+35]):
                    genFound = 1
            for i in range(8, 21):
                if(generos[i-8] == 'true' and  generos[i-8] == row[i+35]):
                    catFound = 1
            if(genFound == 1 and catFound == 1):
                salidaCSV.writerow([row[35], row[36], row[37], row[38], row[39], row[40], row[41], row[42], 
                    row[43], row[44], row[45], row[46], row[47], row[48], row[49], row[50], row[51], row[52], row[53], row[54], row[55], 
                    row[8], row[11], row[14], row[16], row[58]])