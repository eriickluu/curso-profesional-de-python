# VIDEO - Múltiples valores de entrada y salida

# -Comúnmente las funciones tomaran datos de entrada y retornaran un resultado
# -Los datos de entrada se le conocen como parámetros
# -Los valores que colocas al momento de llamar una función se le conocen como argumentos

def crear_mensaje(nombre):
    mensaje = "Hola {}, bienvenido al curso de python 3".format(nombre)
    return mensaje

print(crear_mensaje("Erick"))

def suma(val1, val2, val3):
    return val1 + val2 + val3

res = suma(10,20,30)
print(res)

def obtener_curso():
    return "Curso de python", "Básico", 3.6

curso, nivel, version = obtener_curso()
print(curso, nivel, version)