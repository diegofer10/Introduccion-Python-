"""
#Estructuras de Condicional IF , ELSE,

Operadores para comparar 
==  significa igual 
!= diferente
< menor q 
> mayor q
<= menor igual q 
>= mayor igual q
!= diferente

"""



# Ejemplo N1 
# Si el usuario es Admin, el sistema me debe mostrar un print de bienvenido

user = 'Admin'
if user=='Admin':
    print (f"Bienvenido: {user}")


# Ejemplo N2 
# Si el usuario es Admin, el sistema me debe mostrar un print de bienvenido sino usuario incorrecto

user_ejemplo2 = 'Pepe'
if user_ejemplo2 =='Admin':  #  if user_ejemplo2 =='Pepe' 
    print (f"Bienvenido: {user_ejemplo2}")
else:  
    print ("Usuario Incorrecto")
 

# Ejemplo N3 
# Si edad mayor igual a 21 persona mayor de edad sino es menor 

edad = 25
if edad>=21:   
    print ("Persona mayor de edad")
else:  
    print ("Persona menor de edad")