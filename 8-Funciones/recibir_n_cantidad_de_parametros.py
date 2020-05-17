# VIDEO - Recibir N cantidad de parámetros

# -Se pueden poner valores por default en los parámetros
# -Cuándo un parámetro tiene un valor por default nosotros podemos omitir el argumento
# -No es buena practica asignar un valor a un parámetro con espacio

def crear_usuario(nombre='', apellido='', edad=10):
    return {
        'nombre': nombre,
        'apellido': apellido,
        'nombre_completo': "{} {}".format(nombre, apellido),
        'edad': edad
    }

codi = crear_usuario("Codi", "Facilito", 6)

# Asiganar argumentos por el nombre de los parametros y nose es necesario seguir un orden
codi = crear_usuario(edad=20, apellido="Lucio", nombre="Erick")

print(codi["nombre"])
print(codi["apellido"])
print(codi["edad"])
