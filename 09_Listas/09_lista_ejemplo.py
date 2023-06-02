"""
Lista es un array una coleccion de datos 
"""

#Ejemplo 1 Muestra marca de autos  

marcas = ["Ford","Chevrolet","Fiat","Renault","Toyota","Honda"]
print (marcas)

#Ejemplo 2 lista de numeros del 1 al 10
numeros = list (range(1,11))
print(numeros) 



#Ejemplo 3 Indicies 

marcas = ["Ford","Chevrolet","Fiat","Renault","Toyota","Honda"]
print (marcas[0]) #Indice 0 = Ford
print (marcas[1]) #Indice 1 = Chevrolet
print (marcas[0:3]) #Indice 0 al 3  = "Ford","Chevrolet","Fiat"
print (marcas[0:])  #Todos

#Reasigno a Ford x Mercedez Benz
marcas[0]= "Mercedez Benz"
print (marcas)

# Agregar 
marcas.append ("Ford")
marcas.append ("Volvo")
print (marcas)

#Recorrer con for
nueva_marca=""
print ("PARAR  con S")
#while nueva_marca != "S":
   # nueva_marca = input("Ingrese Marca: ")
  #   marcas.append (nueva_marca)

for marca in marcas:
    print (f" {marcas.index(marca) + 1 }-{marca}")



# Multidimensional - Listas con otras Listas 

print("\n Lista de usuarios ") 


usuarios = [
    ['diego','diego@gmail.com'],
    ['juan','juan@gmail.com'],
    ['marcela','marcela@gmail.com'],
    ['lucia','lucia@gmail.com'],
]

#Todo el listado
#print(usuarios)

#Obtener mail de Juan
#print(usuarios  [1][1])


#Listado de Nombres 
for usuario in usuarios: 
    for elemento in usuario:
        if usuario.index(elemento)==0:
            print(f"Nombre: {elemento}")
        else: 
            print(f"Email: {elemento}")
    print ("\n")