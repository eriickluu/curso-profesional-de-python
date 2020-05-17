# VIDEO - Índices y Sublistas

# -A cada elemento de la lista les corresponde un valor en la misma la cual es el índice para referirnos a ellas
# -Se puede trabajar con negativos en las listas y la obtención sera desde el ultimo
# -Si se agrega un índice que no existe tendremos un error

cursos = ["python", "django", "flask", "c", "c++", "c#", "java", "php"]

# Obtener el primer elemento 
curso = cursos[0]
print(curso)

# Obtener el ultimo elemento
curso = cursos[-1]
print(curso)

# Obtener los primeros 3 elementos
sub = cursos[0:3]
print(sub)

# Obtener todos los elementos apartir de un índice
sub = cursos[5:]
print(sub)

# Obtener la lista tal cual
sub = cursos[:]
print(sub)

# Obtener la lista apartir de índices con saltos 
sub = cursos[1:7:2]
print(sub)

# Obtener el inverso de la lista
sub = cursos[::-1]
print(sub)

