"""
#Estructuras de Condicional IF anidados

Operadores para comparar 
==  significa igual 
!= diferente
< menor q 
> mayor q
<= menor igual q 
>= mayor igual q
!= diferente
"""



# Ejercicio Nro 1
"""
Generar el usuario Admin que trabaja en la empresa Pepito.
Si la empresa es disinta entonces muestra mensaje: No trabaja en la empresa Pepito
Si el usuario es distinto Admin  entonces muestra que el Usuario es Incorrecto
Si el usuario es Admin  y la Pasw es Admin entonces ingresa correctamente

"""


nombre_empresa = "Pepito"
user = 'Admin'
pasw = 'Admin1'
 
if nombre_empresa == "Pepito":

    if user=='Admin' and pasw == 'Admin':
        print (f"Bienvenido Usuario: {user}")
    else:
        print ("Usuario Incorrecto")    

else:
    print ("No trabaja en la empresa Pepito")
 