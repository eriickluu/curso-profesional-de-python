# VIDEO - Formato para cadenas y Formato para cadenas pt 2

# -

texto = "Curso de Python 3"

# Genera un nuevo string con la primera letra en mayúscula
resultado = texto.capitalize()
print(resultado)

# Convierte mayúsculas en minúsculas y viceversa
resultado = texto.swapcase()
print(resultado)

# Convierte todas a mayúsculas
resultado = texto.upper()
print(resultado)

# Convierte todas a minúsculas
resultado = texto.lower()
print(resultado)

# Saber si se encuentra en mayúsculas
resultado = texto.upper()
print(resultado.isupper())

# Saber si se encuentra en minúsculas
resultado = texto.lower()
print(resultado.islower())

# Genera un nuevo string con formato de titulo
resultado = texto.title()
print(resultado)

# Remplazar string por otro
resultado = texto.replace("Python", "ruby")
print(resultado)

# Remplazar string por otro pero solo 1 vez
resultado = texto.replace("Python", "ruby", 1)
print(resultado)

# Quitar espacio al inicio y final del string
resultado = texto.strip()
print(resultado)

curso = "Python"
version = "3"

#Formas de agregar las variables al string
resultado = "Curso de %s %s" %(curso, version)

resultado = "Curso de {a} {b}".format(b=version, a=curso)

print(resultado)

print(f"Curso de {curso} {version}")



