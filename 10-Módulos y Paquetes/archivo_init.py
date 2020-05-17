# VIDEO - Archivo Init

# -Es necesario estar en un folder para que python sepa que es un paquete
# -Se puede escribir código en el archivo
# -El archivo se ejecuta cuando el paquete sea utilizado 
# -También se puede utilizar para crear instancias dentro 

from animales import Pinguino
from animales import Jaguar, mi_jaguar

pinguino = Pinguino()
pinguino.nadar()

mi_jaguar.cazar()