"""
Ejercicio de Marcas de Moto 
Se debe indicar que pais son la marca de las moto

"""
marca_moto = "yamaha"
#marca_moto = "Ducati"
#marca_moto = "Indian"

if marca_moto == "yamaha" or marca_moto == "honda" or marca_moto == "suzuki" or marca_moto == "Kawasaki":
    print (" Marca de Origen Japon")

elif marca_moto == "Benelli" or marca_moto == "Ducati" or marca_moto == "Lambretta" or marca_moto == "Piaggio":    
        print (" Marca de Origen Italia")

elif marca_moto == "Harley Davidson" or marca_moto == "Indian" or marca_moto == "American Eagle Motorcycles" or marca_moto == "Chopper":    
        print (" Marca de Origen Estados Unidos")


else: 
    print ("Otros Paises")
    