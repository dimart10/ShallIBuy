## Sobre el proyecto

## Dataset

El dataset usado lo obtenimos de [data.world](https://data.world/craigkelly/steam-game-data), donde está alojado de forma pública para uso académico. El dataset fue creado por [Craigh Kelly](https://data.world/craigkelly) en 2016 con información obtenida de la API de Steam y la página [steamspy.com](https://steamspy.com/). 

Consta de alrededor de 13350 juegos, cada uno con 78 columnas de información. Este dataset no ha sido modificado a la hora de realizar el proyecto, de moodo que el dataset puede obtenerse de la fuente original sin problemas y en caso de que el original se actualizase con datos más recientes debería poder procesarlo correctamente.

En nuestro proyecto solo usamos unas cuantas columnas. Las principales son el precio, la nota media en metacritic, el número de propietarios del juego, recomendaciones y jugadores activos, además de algunos parámetros extra como los sistemas operativos que lo admiten, para dar más información al usuario.

## Diseño y funcionamiento

El proyecto se basa en el modelo map-reduce, usando como lenguaje python. Se realizan 3 fases de map-reduce hasta dar el resultado final.

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

Una vez encontrado el juego se ejecuta la primera fase de map-reduce: Parecidos. 
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

La segunda fase es "Medias", en esta se halla la media numérica de los valores relevantes de los juegos similares (ignorando los 0s, que indican que no se conocen los datos) y se sacan a otro archivo csv "auxMedias.csv"

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
### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/dimart10/ShallIBuy/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://help.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.

### Sobre el proyecto

### Modo de uso

Deberás descargarte el archivo mencionado en el apartado de dataset, junto a los archivos .py necesarios(buscaNombre, mapReduce de parecidos, medias y salida). Una vez descargados abre una shell que tenga instalada python y ejecuta la siguiente linea en ella:

**python buscaNombre.py "(Nombre de tu juego)"** poniendo el juego en cuestion entre las comillas. 

Es muy importante que el juego este exactamente escrito como en el dataset, asi que ten cuidado. Debería salir algo así:

![Inicio](/buscaNombre.jpg)

Una vez hayas encontrado tu juego ejecuta las siguientes líneas en la misma shell:

**python mapper-Parecidos.py | python reducer-Parecidos.py** 

Deberia salir algo así:

![Inicio](/parecidos.jpg)

y a continuación:

**python mapper-Medias.py | python reducer-Medias.py**

Deberia salir algo así:

![Inicio](/medias.jpg)

y para acabar:

**python mapper-Salida.py | python reducer-Salida.py**

Deberia salir algo así:

![Inicio](/salida.jpg)


### Extensiones
### Aprendizaje
### Valoracion / conclusion / futuro
### Nosotros

