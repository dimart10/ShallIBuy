## Shall I Buy?

You can use the [editor on GitHub](https://github.com/dimart10/ShallIBuy/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

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
### Dataset
### Diseño y funcionamiento
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

![Inicio](/salidas.jpg)


### Extensiones
### Aprendizaje
### Valoracion / conclusion / futuro
### Nosotros

