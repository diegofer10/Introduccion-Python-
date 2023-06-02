"""
Diccionarios y Set 
Set:  tipo de dato pero no tiene indice ni orden
Diccionario: tipo de datos que tiene formato parecido a json
"""

#Ejericio 1 definir set de usuarios agregar y eliminar datos
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