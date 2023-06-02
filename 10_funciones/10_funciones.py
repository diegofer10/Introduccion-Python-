"""
Funciones predefinidas 
"""


usuarios =  ['diego','juan','pedro','lucia']
numeros  =  [1,2,3,4,5,6,1, 11 , 1 , 1, 7,80,98,86,33]

#Ordenar una lista
numeros.sort()
print(numeros)

#eliminar numero
numeros.remove(98)
print(numeros)

#Buscar a Juan
print('juan' in usuarios )
#retorna True o False


#Cuantas veces aparece el numero 1 
numeros.append(1)
print(numeros.count(1) )


#Unir listas con extends
usuarios.extend(numeros)
print(usuarios)