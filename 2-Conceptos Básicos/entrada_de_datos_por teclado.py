# VIDEO - Entrada de datos por teclado

# -La función input regresa un valor de tipo string si se necesita trabajar con otro tipo de datos se tiene que convertir

# print("¿Cúal es tu nombre?")
# nombre = input()
# print("Hola", nombre)
nombre = input("¿Cúal es tu nombre?\n")

# print("¿Cúal es tu edad?")
# edad = int(input())
# print("Edad", edad)
edad = int(input("¿Cúal es tu edad?\n"))

# print("¿Cúal es tu peso?")
# peso = float(input())
# print("Peso", peso)
peso = float(input("¿Cúal es tu peso?\n"))

# print("¿Estas Autorizado?(si/no)")
# autorizado = input() == "si"
autorizado = input("¿Estas Autorizado?(si/no)\n") == "si"

print("Hola", nombre)
print("Edad", edad)
print("Peso", peso)
print("Autorizado", autorizado)