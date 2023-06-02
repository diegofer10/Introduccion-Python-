"""
*********************
Estructura for
*********************
"""

#Ejercicio 1: Mostrar numeros de 0 a 5
numero = 0 
#Muestra numero del 1 al 5
for numero in range (0,6):
    print(numero)
############################################################
############################################################


#Ejercicio 2: Tabla de Multipicar segun numero ingresado
print('-----------------TABLA---------------- ')
num = int(input("Ingrese Numero de Tabla: "))

#valido que el numero sea mayor a 0 
if num < 0 or num> 11: 
    print ('Numero incorrecto')
    #Valor por defecto
    num = 1 
   

#Muestra numero del 1 al 10
for tabla in range (1,11):
    print(f" {tabla} x {num}= {num*tabla}" )
else:
    print("Tabla Finalizada" )


