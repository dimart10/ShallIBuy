#!/usr/bin/python
from decimal import Decimal
import sys
import re
import csv

atributos = ["nota de metacritic", "recomendaciones", "numero de propietarios", "numero de jugadores", "precio", "-Fecha de lanzamiento: ", "-Soporta Mando: ", "-Es gratis: ", "-Windows: ", "-Linux: ", "-Mac: "]
i = 0
score = 0

print ("")
print ("----------------------VALORACIONES-------------------")
print ("")

for line in sys.stdin:
	try:
		comp = float(line)
		score += comp
		dec = round(comp,2)
		if float(line) >= 0:
			print ("-En el atributo " + atributos[i] + " el juego en cuestion es " + str(dec) + " veces superior a la media.")
		elif float(line) < 0:
			print ("-En el atributo " + atributos[i] + " el juego en cuestion es " + str(dec) + " veces inferior a la media.")

	except ValueError:
		print (atributos[i] + line)

	print ("")
	i+=1

print ("Puntuacion final: " + str(score))

if score > 10:
	print "Un juego muy recomendable, muy superior a los de su tipo"
elif score > 5:
	print "El juego es bastante decente entre los de su tipo"
elif score > 0:
	print "Juego mediocre, encontraras mejores de su tipo"
else:
	print "Juego muy inferior a los demas, no se recomienda"

print ("")
print ("-----------------------------------------------------")
print ("")
	