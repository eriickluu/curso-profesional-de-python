# VIDEO - De listas a tuplas

# -Debes saber cuando usar lista y cuando tuplas

lista = ["Curso", "Python", "CodigoFacilito" ]
tupla = ("Introducción", "Básico", "Listas", "Tuplas")

# Convertir una tupla a lista
nueva_lista = list(tupla)
print(nueva_lista)

# Convertir una lista a tupla
nueva_tupla = tuple(lista)
print(nueva_tupla)

# Convertir string a tupla y lista

mensaje = "Este es el curso de Python"

nueva_lista = list(mensaje)
nueva_tupla = tuple(mensaje)

print(nueva_lista)
print(nueva_tupla)