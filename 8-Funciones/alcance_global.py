# VIDEO - Alcance global

# -Las variables fuera de funciones son variables globales 
# -Cada vez que se define una función define su propio contexto 
# -Si se quiere modificar el valor de una variable global dentro de una función se utilizara "global"

animal = "León"

def mostrar_animal():
    global animal
    animal = 'Ballena'
    print(animal)

mostrar_animal()
print(animal)
