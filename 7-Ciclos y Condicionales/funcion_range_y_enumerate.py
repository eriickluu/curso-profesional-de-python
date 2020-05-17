# VIDEO - Función Range y enumerate 

# -Ambas funciones se usan mucho en conjunto a un for

for valor in range(10):
    print(valor)

for valor in range(1, 20):
    print(valor)

for valor in range(-10, 10):
    print(valor)

for valor in range(1, 101, 2):
    print(valor)

lista = [1,2,3,4,5,6]
for indice in range(len(lista)):
    print("Indice",indice,"Valor", lista[indice])

lista = [1,2,3,4,5,6]
for indice, valor in enumerate(lista):
    print("Indice",indice,"Valor", valor)

lista = [1,2,3,4,5,6]
for indice, valor in enumerate(lista, 10):
    print("Indice",indice,"Valor", valor)