# VIDEO - Paquetes

# -Un paquete no es mas que una carpeta el cual contiene módulos
# -Al crear un paquete se debe de crear un archivo llamado "__init__.py" con esto python sabrá que el folder es un paquete 

from animales.aves import Pinguino

pinguino = Pinguino()
pinguino.nadar()