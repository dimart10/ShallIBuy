## Sobre el proyecto

Shall I Buy es una aplicación de asesoramiento de compra de videojuegos en la plataforma de venta digital Steam. El objetivo final es ofrecer una serie de características objetivas sobre un juego por el que pregunte el usuario, con el fin de indicarle si las valoraciones críticas están por encima o por debajo de la media, si el juego consta de una comunidad activa, o del precio por ejemplo. Con estos valores obtenidos y analizados, se le indica al usuario si merece la pena obtener el juego en cuestión, o hay mejores opciones dentro del mismo género o tipo de juego que puedan ofrecer más al usuario.  

Si eres un usuario, esperamos que Shall I Buy le resulte tanto útil como cómodo a la hora de utilizarlo. A continuación explicamos en más detalle todas las características del proyecto. 


## Dataset

El dataset usado lo obtenimos de [data.world](https://data.world/craigkelly/steam-game-data), donde está alojado de forma pública para uso académico. El dataset fue creado por [Craigh Kelly](https://data.world/craigkelly) en 2016 con información obtenida de la API de Steam y la página [steamspy.com](https://steamspy.com/). 

Consta de alrededor de 13350 juegos, cada uno con 78 columnas de información. Este dataset no ha sido modificado a la hora de realizar el proyecto, de moodo que el dataset puede obtenerse de la fuente original sin problemas y en caso de que el original se actualizase con datos más recientes debería poder procesarlo correctamente.

En nuestro proyecto solo usamos unas cuantas columnas. Las principales son el precio, la nota media en metacritic, el número de propietarios del juego, recomendaciones y jugadores activos, además de algunos parámetros extra como los sistemas operativos que lo admiten, para dar más información al usuario.

## Diseño y funcionamiento

El proyecto se basa en el modelo map-reduce, usando como lenguaje python. Se realizan 3 fases de map-reduce hasta dar el resultado final.

### Búsqueda inicial
Antes de la primera fase map-reduce se busca al juego indicado por el usuario en el dataset y, si lo encuentra, guarda sus datos relevantes en un csv auxiliar "auxName.csv".

**[buscaNombre.py](https://github.com/dimart10/ShallIBuy/blob/master/ProyectoMapReduce/buscaNombre.py)**
```python
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
```

### Fase 1 (Parecidos)
En esta fase se buscan en el dataset los juegos que compartan al menos una categoría y tag con el juego a evaluar, de este modo se obtiene en otro csv "auxParecidos.csv" los datos relevantes de los juegos con los que lo compararemos.

**[mapper-Parecidos.py](https://github.com/dimart10/ShallIBuy/blob/master/ProyectoMapReduce/mapper-Parecidos.py)**
```python
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
 ```

**[reducer-Parecidos.py](https://github.com/dimart10/ShallIBuy/blob/master/ProyectoMapReduce/reducer-Parecidos.py)**
```python
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
```

### Fase 2 (Medias)
En esta se halla la media numérica de los valores relevantes de los juegos similares (ignorando los 0s, que indican que no se conocen los datos) y se sacan a otro archivo csv "auxMedias.csv"

**[mapper-Medias.py](https://github.com/dimart10/ShallIBuy/blob/master/ProyectoMapReduce/mapper-Medias.py)**
```python
import sys
import re
import csv

with open('auxParecidos.csv') as csvfile:

	reader = csv.reader(csvfile)

	for row in reader:
		 for i in range(0, 5):
		 	print row[i],
		 print "\n",
 ```

**[reducer-Medias.py](https://github.com/dimart10/ShallIBuy/blob/master/ProyectoMapReduce/reducer-Medias.py)**
```python
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
	print("Medias calculadas")
```

### Fase 3 (Salida)
En esta se opera sobre las medias obtenidas en la fase anterior y las compara con los valores del juego en auxName.csv. Finalmente, muestra el resultado de estas comparaciones por consola y da un veredicto sobre el juego.

**[mapper-Salida.py](https://github.com/dimart10/ShallIBuy/blob/master/ProyectoMapReduce/mapper-Salida.py)**
```python
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
 ```

**[reducer-Salida.py](https://github.com/dimart10/ShallIBuy/blob/master/ProyectoMapReduce/reducer-Salida.py)**
```python
from decimal import Decimal
import sys
import re
import csv

atributos = ["nota de metacritic", "recomendaciones", "numero de propietarios", "numero de jugadores", "precio", "-Fecha de lanzamiento: ", "-Soporta Mando: ", "-Es gratis: ", "-Soporta Windows: ", "-Soporta Linux: ", "-Soporta Mac: "]
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
```
## Modo de uso

Deberás descargarte el archivo mencionado en el apartado de dataset, junto a los archivos .py necesarios(buscaNombre, mapReduce de parecidos, medias y salida). Una vez descargados abre una shell que tenga instalada python y ejecuta la siguiente linea en ella:
```
python buscaNombre.py "(Nombre de tu juego)" 
```
Poniendo el juego en cuestion entre las comillas. Es muy importante que el juego este exactamente escrito como en el dataset, asi que ten cuidado. Debería salir algo así:

![Inicio](/buscaNombre.jpg)

Una vez hayas encontrado tu juego ejecuta las siguientes líneas en la misma shell:
```
python mapper-Parecidos.py | python reducer-Parecidos.py
```
Deberia salir algo así:

![Inicio](/parecidos.jpg)

y a continuación:
```
python mapper-Medias.py | python reducer-Medias.py
```
Deberia salir algo así:

![Inicio](/medias.jpg)

y para acabar:
```
python mapper-Salida.py | python reducer-Salida.py
```
Deberia salir algo así:

![Inicio](/salida.jpg)


## Posibles mejoras y extensiones

Nuestra aplicación hace su trabajo, pero es limitada. Para mejorar este proyecto habíamos pensado en varias modificaciones o extensiones que podrían servir para mejorar la aplicación en un futuro:
- **Limpieza del código**. Algunas partes del código no son tan entendibles como deberían, en parte debido a nuestro poco conocimiento de python. En particular sería deseable que los números de las columnas estuvieran guardados en un fichero auxiliar.

- **Script**. La aplicación sería más cómoda de usar si hubiera un script que se encargara de llamar a los diferentes archivos y que gestionase la interacción con el usuario.

- **Mejorar el algoritmo**. Además de las mejoras de eficiencia que muy probablemente se podrían hacer a nuestro algoritmo, también sería interesante usar más atributos del dataset a la hora de calcular la valoración del juego.

- **Dataset**. El dataset que utilizamos, si bien nos proporciona los datos que buscábamos, está desactualizado pues se creo en el año 2016, y no se corresponde con el estado actual de la plataforma. Un dataset más actual y con más datos permitiría mejorar notablemente la precisión de la aplicación, aunque requiriera cierto trabajo adaptarla a este.

- **Historial de ofertas**. En la idea original de este proyecto además de decir al usuario si debería comprar un juego, se quería decirle en que momento sería mejor hacerlo. Para esto pensamos utilizar un dataset con datos históricos sobre las ofertas de los juegos. Sin embargo, no encontramos ningún dataset de estas cualidades, ya que esa información no está disponible desde la api de steam y no hay ninguna recopilación de datos pública. 

## Conclusión y valoración general de proyecto

A la hora de realizar este trabajo, nos hemos ido encontrando con diversos problemas. Los problemas iniciales han surgido en gran medida del poco conocimiento previo que poseíamos sobre las tecnologías y métodos utilizados. No estábamos familiarizados con el uso de Linux, al cual nos hemos ido acostumbrando. Además, nunca habíamos programado en Python, por lo que surgieron varios problemas de código.
El desconocimiento o mal uso de lo anterior dicho hizo que no pudiéramos planificar del todo bien, ya que no sabíamos la cantidad de tiempo estimada que nos llevaría cada parte del proyecto. A todo esto se añadió la suma de entregas de trabajos y exámenes no planificados de otras asignaturas que cursamos, haciendo más difícil aún el desarrollo normal de este proyecto.

A pesar de los inconvenientes, nos hemos quedado con un buen sabor de boca. La aplicación que hemos desarrollado ha cumplido con lo que prometía; es sencilla, pero funcional. Sabemos que probablemente no es un proyecto que pueda parecer muy grande a primera vista, pero tiene mucho trabajo de aprendizaje de fondo.

También nos hemos dado cuenta de que las metodologías utilizadas para realizar el proyecto (y la asignatura en general) son bastante interesantes, además de extensibles. Los conocimientos que hemos adquirido a lo largo de la asignatura pueden llegar a sernos útiles de cara al futuro, ya que tiene mútliples aplicaciones posiblemente relacionadas con nuestros intereses.

Podemos decir que los resultados obtenidos han superado con creces a las dificultades que hemos tenido para hacerlo.

## Sobre nosotros

Somos un grupo de estudiantes del grado de Desarrollo de Videojuegos en la Universidad Complutense de Madrid (UCM), nuestros nombres son:
- [Diego Martínez](https://github.com/dimart10)
- [Gonzalo Sanz](https://github.com/gonzsa04)
- [Alberto Casado](https://github.com/alcasa04)
- [Héctor Marcos](https://github.com/hectormr98)

El proyecto lo realizamos para la asignatura Cloud and Big Data, con el fin de aplicar los conceptos aprendidos. El resultado final es éste. Esperamos que sea de su agrado.

## Enlaces

- [Página en GitHub del proyecto](https://github.com/dimart10/ShallIBuy)
