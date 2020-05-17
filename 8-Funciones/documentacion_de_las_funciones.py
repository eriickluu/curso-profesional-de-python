# Cómo mencionamos anteriormente, una vez que nosotros definimos una función, podemos llamarla n cantidad de veces, inclusive, fuera de nuestro script, cómo lo veremos más adelante (módulos y paquetes) es por ello que una muy buena practica de programación es documentar nuestras funciones.

# Para que nosotros podamos documentar una función lo haremos mediante un comentario, comentario, el cual debe de encontrarse dentro de la función y utilizando triples comillas dobles, cómo podemos observar en el siguiente ejemplo.

def mi_funcion(*args):
  """Esta es la documentación de mi_función"""
  print(args)

# Recordemos que al utilizar triples comillas dobles podemos colocar un comentario con saltos de línea.

# Podemos trabajar con la documentación a través de su atributo ____doc____

print(mi_funcion.__doc__)

# Ahora veamos un ejemplo en el cual podemos sacar provecho a nuestra documentación.

def suma(a, b):
  """Función suma"""
  return a + b

def resta(a, b):
  """Función resta"""
  return a - b

opciones = {'a' : suma, 'b': resta}
print("Ingrese la opción deseada")

for opcion, funcion in opciones.items():
  mensaje = '{}) {}'.format(opcion, funcion.__doc__)
  print(mensaje)

opcion = input("Opción : ")

# Almacenamos las funciones dentro de nuestro diccionario, posteriormente iteramos los elementos del diccionario y en cada iteración imprimimos la documentación.