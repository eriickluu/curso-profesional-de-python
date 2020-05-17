# VIDEO - Cadena de caracteres

# -Se puede trabajar los string como listas

lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"

separador = "; "

# Separar nuestro string por espacio
resultado = lenguajes.split()
print(resultado)

# Separar nuestro string por ;
resultado = lenguajes.split(";")
print(resultado)

# Separar nuestro string por ; y espacio
resultado = lenguajes.split(separador)
print(resultado)

# Crear lista a string
nuevo_string = separador.join(resultado)
print(nuevo_string)

# Convertir strings a listas con saltos de linea
texto = """
Este es un texto
con
saltos
de
línea
"""

resultado = texto.splitlines()
print(resultado)