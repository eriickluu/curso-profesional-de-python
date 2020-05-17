# VIDEO - Qué son los diccionarios

# -Los diccionarios permiten almacenar diferentes tipos de datos (cadenas, enteros, listas, tuplas e incluso otros diccionarios) 
# -Son mutables 
# -No se rigen pon índices si no por llave
# -Todos los valores necesitan una llave y una llave un valor
# -Sí se quiere agregar más valores basta con separarlos mediante una coma 
# -Comúnmente las llaves suelen ser strings
# -El equivalente a un json en python es un diccionario

# Diccionario vacío
diccionario = { }
diccionario = dict()

# { llave : el valor el cual queremos asociar. }
diccionario = { "total": 55 }

diccionario = { "total": 55, "descuento": True, "subtotal": 200 }

diccionario = { "total": 55, 10: "Curso de Python", (1,2,3): True }

# Llaves

# Un string ("total")
# Un número enero (10)
# Una tupla que almacena números enteros (1,2,3)

usuario = {
    'nombre': 'Nombre del usuario',
    'edad': 23,
    'curso': 'Curso de Python',
    'skills': {
        'programacion': True,
        'base_de_datos': False
    },
    'medallas': ['básico', 'intermedio']
}

diccionario = { 'Eduardo': 1, 'Fernando': 2, 'Uriel': 3, 'Rafael': 4 }

# Obtener todas las llaves de un diccionario
diccionario.keys()

# Obtener todos los valores de un diccionario
diccionario.values()

# Recorrer llave y valor de un diccionario
for key, value in diccionario.items():
    print(key, value)

usuario = {
    'name': 'Erick Adrián',
    'age': 20,
    'job': 'UANL'
}

calificaciones = usuario.get('calificaciones', [])
if calificaciones:

    for calificacion in calificaciones:
        print(calificacion)

usuarios = ['Erick', 'Adrián', 'Lucio']
diccionario = { usuario: position + 1 
                    for position,usuario in enumerate(usuarios) }
            
print(diccionario)