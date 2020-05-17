# VIDEO - Break y continue

# -Permite modificar el comportamiento del los ciclos
# -Break finaliza el ciclo
# -Continue hace que el ciclo salte a la siguiente iteración

titulo = "Curso de Python 3"

for caracter in titulo:
    if caracter == "P":
        break
    print(caracter)

for caracter in titulo:
    if caracter == "P":
        continue
    print(caracter)