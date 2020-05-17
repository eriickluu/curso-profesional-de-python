# VIDEO - Formas de imports

# -Existen diferentes formas de importar
# -El signo * en el import indica que se trae todo del Modulo
# -Se puede cambiar el nombre con los imports poniendo un "as"

# from calculadora import *
from calculadora import suma, resta as resta_renombrada

resultado = resta_renombrada(10, 20)
print(resultado)