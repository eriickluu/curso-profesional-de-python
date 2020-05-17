# Los siguientes, son una serie de ejercicios que tienen como finalidad el que tu practiques los conocimientos adquiridos a lo largo de estos bloques.

# Dado un diccionario, el cual almacena las calificaciones de un alumno, siendo las llaves los nombres de las materia y los valores las calificación, mostrar en pantalla el promedio del alumno.
# Ejemplo: calificaciones = {calculo:10, dibujo:5}

# calificaciones = {
#     'programacion': 9,
#     'matematicas': 10,
#     'fisica': 5,
#     'hacking': 10,
#     'diseño': 8
# }

# suma = 0

# for valor in calificaciones.values():
#     suma += valor

# promedio = suma / len(calificaciones)
# print("El promedio es:", promedio)

# A partir del diccionario del ejercicio anterior, mostrar en pantalla la materia con mejor promedio.

# cali =  calificaciones.values()
# print("La materia con mejor promedio es:", max(cali))

# Crear una lista la cual almacene 10 números positivos ingresados por el usuario, mostrar en pantalla: la suma de todos los números, el promedio, el número mayor y el número menor.

# lista = []
# suma = 0

# for numero_veces in range(0, 10):
#     lista.append(int(input("Ingresa el número {}:".format(numero_veces+1)))) 
#     suma += lista[numero_veces]

# print("La suma de todos los númerosla suma de todos los números es:", suma)

# promedio = suma / len(lista)
# print("El promedio es:", promedio)

# numero_mayor = max(lista)
# print("El número mayor es:", numero_mayor)

# numero_menor = min(lista)
# print("El número menor es:", numero_menor)

# Dado una lista de frases ingresadas por el usuario, mostrar en pantalla todas aquellas que sean palíndromo.

# lista = []

# veces_frase = int(input("Cuantas frases desea ingresar:"))

# for numero in range(0, veces_frase):
#     frase = str(input("Ingrese la frase número {}:".format(numero+1)))
#     lista.append(frase)

# # print(lista)

# for frase in lista:
#     frase_minuscula_sin_espacios = frase.lower().replace(" ", "")
#     frase_invertida = frase_minuscula_sin_espacios[::-1]

#     if frase.replace(" ", "").lower() == frase_invertida:

#         print("La frase número {} es palíndromo.".format(numero+1))
#         print("Frase ingresada fue:" , frase)

# Mostrar en pantalla la palabra que más se repita junto con la cantidad de veces que lo hace del capituló número uno de Frankenstein

# Remplazar cada letra de una frase dada por el usuario por la posición que le corresponde en el abecedario y mostrar el nuevo string en pantalla. (Los espacios no se remplazan) . Ejemplo: frase : 'Hola' salida : 815121 H(8) o(15) l(12) a(1)

# Mostrar en pantalla la cantidad de vocales que existe en una frase dada por el usuario.

# Mostrar en pantalla la frecuencia de aparición de vocales en una frase dada por el usuario.
# Ejemplo : 'Hola Mundo' salida : o=2, a=3, u=1

# frase = str(input("Ingresa una frase:"))

# for letra in frase:
    
# Eliminar todas las vocales de una frase dado por el usuario y mostrar el nuevo string en pantalla.

# Listar todos los números pares del 0 al 100