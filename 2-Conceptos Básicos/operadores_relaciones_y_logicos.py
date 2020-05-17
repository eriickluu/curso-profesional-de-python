# VIDEO - Operadores relacionales y lógicos

# -Con los operadores relacionales son para comparar 2 valores y tener como resultado un valor boleano verdadero o falso
# -Los operadores relacionales son 6
# -Con los operadores lógicos de igual forma se obtiene una salida de tipo boleano es decir verdadero o falso
# -Los operadores lógicos son 3 

variable_uno = 10
variable_dos = 10

mayor = variable_uno > variable_dos
menor = variable_uno < variable_dos
mayor_igual = variable_uno >= variable_dos 
menor_igual = variable_uno <= variable_dos
# igual = variable_uno == variable_dos
igual = variable_uno is variable_dos
# diferente = variable_uno != variable_dos
diferente = variable_uno is variable_dos

# Todas las comparaciones tienen que ser verdaderas para que el resultado sea verdadero 
resultado_and = True and True and diferente
# Por lo menos 1 comparación tiene que ser verdadera para que el resultado sea verdadero 
resultado_or = True or True or diferente
# Dara verdaro cuando el operador sea falso y viseversa
resultado_not = not False

print(mayor)
print(menor)
print(mayor_igual)
print(menor_igual)
print(igual)
print(diferente)

print(resultado_and)
print(resultado_or)
print(resultado_not)

