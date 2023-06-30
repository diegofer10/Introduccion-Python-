"""
Diccionarios y Set 
Set:  El tipo set en Python es la clase utilizada por el lenguaje para representar los conjuntos. 
      Un conjunto es una colección desordenada de elementos únicos, es decir, que no se repiten.

Diccionario:  Un diccionario en Python es una estructura de datos que permite almacenar cualquier tipo de información, desde cadenas de texto o caracteres hasta números enteros, con decimales, listas e incluso otros diccionarios. Al igual que sucede con un diccionario de lengua, los datos se encuentran ordenados utilizando una clave única para cada uno de ellos, lo que permite localizar cada uno de los datos de una forma muy rápida. 
Los diccionarios Python son mutables, esto quiere decir que no tienen un tamaño predefinido y que su contenido aumenta o disminuye según las necesidades de la aplicación. Todos los datos son también modificables, es decir, se puede añadir, modificar, eliminar y consultar todos los datos de una manera sencilla y rápida.
Se trata de una estructura de datos similar a las listas, las tuplas o los conjuntos. Se utilizan básicamente para almacenar una gran cantidad de datos de forma ordenada

#Ejericio 1 definir set de usuarios agregar y eliminar datos
"""

 
usuarios =  {
    'diego','juan','pedro','lucia'
    }

print( usuarios)

#agregar 
usuarios.add('ana')
usuarios.add('juana')

#eliminar
usuarios.remove('pedro')



#Ejericio 2 Diccionarios


usuarios =  {
    "nombre":"diego",
    "email":"diego@gmail.com"
   
    }


print (usuarios)
print (usuarios["email"])

#Lista asociada

usuarios =  [
    {    "nombre":"diego",    "email":"diego@gmail.com"     },
    {    "nombre":"juan",    "email":"juan@gmail.com"     },
    {    "nombre":"marcos",    "email":"marcos@gmail.com"     }
    ]

print (usuarios)
print (usuarios[0]["nombre"])  #Nombre Diego
print (usuarios[1]["nombre"])  #Nombre Juan



#Muestro todos los nombre del diccionario
for usuario in usuarios:
    print (f"Nombre : {usuario['nombre']}") 
