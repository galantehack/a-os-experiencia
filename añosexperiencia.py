
def experiencia():
    print("vamos a ver si estas acto para el trabajo")
    
    años="s" #inicio la variable año 
    while años != "s" or "S":   #mientras que año sea diferente a s o S se va a ejecutar repetidamente el codigo
        años = int(input( "ingresa cuantos años tienes de experiencia  y S para salir: " )) # usuario agrega opcion 
        #los if que dan las condiciones para mostrar resultado 
        if años <= 1:
           print("eres un programador junior novato")
        if años in range(1, 3):
           print("eres un programador semi senior , aun te falta")
        elif años in range(3 , 5):
           print(" ya eres senior , puedes programar ")
        elif años >= 5:
           print(" eres la cabra de la programacion")
experiencia() # se llama la funcion para que el codigo sea ejecutado 