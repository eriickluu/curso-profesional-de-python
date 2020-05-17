# VIDEO - Operadores comunes

# -Todos estos métodos aplican para listas que también contienen solo strings

lista = [8.17, 90, 1, 5, 44, 1.32]

# Ordena la lista de forma ascendente
lista.sort()
print(lista)

# Ordena la lista de forma descendente
lista.sort(reverse=True)
print(lista)

# Obtener el número mayor
lista.sort(reverse=True)
mayor = lista[0]
print(mayor)

mayor = max(lista)
print(mayor)

# Obtener el número menor
lista.sort()
menor = lista[0]
print(menor)

menor = min(lista)
print(menor)

# Obtener la longuitud de una lista
longuitud = len(lista)
print(longuitud)

# buscar un elemento en la lista
resultado = 8.17 in lista
print(resultado)

# buscar en que index se encuentra un elemento en la lista
indice = lista.index(8.17)
print(indice)

# Cuantas veces se encuentra un elemento en la lista
contador = lista.count(5)
print(contador)

