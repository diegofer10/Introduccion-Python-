"""
*********************
Estructura while
*********************
"""
#Ejericio: Muestra numeros del 1 al 5

contador = 1 
while contador <=5:
    print(f"contador: {contador} ")
    contador=contador+1


#Ejericio2: Muestra numeros del 1 al 50 separados por , 
print('------------EJERCICIO 2----------')
contador2 = 1 
muetra = str(0)

while contador2 <=50:
    muetra=muetra + ","+str(contador2)
    contador2=contador2+1

print(muetra)


#Ejericio3: Tabla de Multiplicar  
print('------------EJERCICIO 3----------')
num = int(input("Ingrese Numero de Tabla: "))

#valido que el numero sea mayor a 0 
if num < 0 or num> 11: 
    print ('Numero incorrecto')
    #Valor por defecto
    num = 1 


contador3= 1
while contador3 <=10:   
    print(f" {contador3} x {num}= {num*contador3}" )
    contador3=contador3+1

 