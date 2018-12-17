#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import re

categorias = sys.stdin.readline()
categorias = re.split(' ', categorias)
categorias.pop()

generos = sys.stdin.readline()
generos = re.sub('\n', '', generos)
generos = re.split(' ', generos)

with open('games_features.csv') as csvfile:
    reader = csv.reader(csvfile)
    numFilas = 0
    with open('auxParecidos.csv', 'wb') as csvfile:
        salidaCSV = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            genFound = 0
            catFound = 0
            for i in range(0, 8):
                if(categorias[i] == 'true' and categorias[i] == row[i+35]):
                    genFound = 1
            for i in range(8, 21):
                if(generos[i-8] == 'true' and  generos[i-8] == row[i+35]):
                    catFound = 1
            if(genFound == 1 and catFound == 1):
                salidaCSV.writerow([row[9], row[12], row[15], row[17], row[58]])
        print("Juegos parecidos encontrados")
