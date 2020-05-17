# VIDEO - Formas de terminar una función

# -Si no se indica un valor a retornar en la función por defecto sera "None"
# -La función termina donde pongas el return

def mi_funcion():
    print("un mensaje")
    return 2

resultado = mi_funcion()
print(resultado)

def mi_funcion_2(parametro):
    if parametro:
        return 100

resultado = mi_funcion_2("")
print(resultado)