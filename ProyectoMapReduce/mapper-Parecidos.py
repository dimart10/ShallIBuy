#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import re


with open('auxName.csv') as csvfile:
    readerName = csv.reader(csvfile)
    row = readerName.next()
    for i in range(0, 8):
          print row[i],

    print "\n",

    for i in range(8, 21):
          print row[i],
 
