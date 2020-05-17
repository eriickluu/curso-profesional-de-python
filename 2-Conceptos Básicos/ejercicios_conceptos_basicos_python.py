# Los siguientes, son una serie de ejercicios que tienen como finalidad el que tu practiques los conocimientos adquiridos a lo largo de este segundo bloque.

# Dado de los valores ingresados por el usuario (base, altura) calcular y mostrar en pantalla el área de un triángulo.

base = float(input("Ingrese la base:"))
altura = float(input("Ingrese la altura:"))
area_triangulo = (base * altura) / 2
print("El área de un triángulo es:", area_triangulo) 

# Convertir la cantidad de dólares ingresados por un usuario a pesos colombianos y mostrar el resultado en pantalla.

dolares = float(input("Ingrese la cantidad de dólares:"))
pesos_colombianos = dolares * 4029.00
print("En pesos colombinos son:", pesos_colombianos)

# Convertir los grados centígrados ingresados por un usuario a grados Fahrenheit y mostrar el resultado en pantalla.

grados_centigrados = float(input("Ingrese los grados centígrados:"))
grados_fahrenheit = (grados_centigrados * 1.8000) + 32.00
print("En grados Fahrenheit son:", grados_fahrenheit)

# Mostrar en pantalla la cantidad de segundos que tiene un lustro.

lustro = 5 * 365 * 24 *60 * 60
print(lustro)

# Calcular la cantidad de segundos que le toma a la luz viajar del sol a Marte y mostrar el resultado en pantalla.

luz_a_marte = 12.5 * 60
print(luz_a_marte)

# Calcular el número de vueltas que da una llanta en 1 km, dado que el diámetro de la llanta es de 50 cm, mostrar el resultado en pantalla.

# circunferencia = 3.1416 * 50
# vueltas_llanta = 

# Calcular y mostrar en pantalla la longitud de la sombra de un edificio de 20 metros de altura cuando el ángulo que forman los rayos del sol con el suelo es de 22º.

# Mostrar en pantalla True o False si la edad ingresada por dos usuarios es la misma.

edad_usuario_1 = int(input("Ingrese la edad usuario 1:"))
edad_usuario_2 = int(input("Ingrese la edad usuario 2:"))
comparacion = edad_usuario_1 is edad_usuario_2
print(comparacion)

# Mostrar en pantalla la cantidad de meses transcurridos desde la fecha de nacimiento de un usuario.

# Tenemos un artículo en donde explicamos más en detalle el trabajo con fechas

# from datetime import date

# dia = int(input("Ingrese su dia de nacimiento \n"))
# mes = int(input("Ingrese su mes de nacimiento \n"))
# anno = int(input("Ingrese su año de nacimiento \n"))

# dia_actual = int("{}".format(today.day))
# mes_actual = int("{}".format(today.month))
# anno_actual = int("{}".format(today.year))

# cantidad_de_meses = anno_actual - anno

# if (mes > mes_actual):
#     cantidad_de_meses-=1
#     cantidad_de_meses = cantidad_de_meses * 12
# cantidad_de_meses = cantidad_de_meses + 12 - mes + mes_actual
# if (dia > dia_actual):
#     cantidad_de_meses -=1

# print("Haz vivido", cantidad_de_meses, "meses.")

# Mostrar en pantalla el promedio de un alumno que ha cursado 5 materias (Español, Matemáticas, Economía, Programación, Ingles).

material_español = float(input("Ingresa tu calificación de Español:"))
material_matematicas = float(input("Ingresa tu calificación de Matemáticas:"))
material_economia = float(input("Ingresa tu calificación de Economía:"))
material_programacion = float(input("Ingresa tu calificación de Programación:"))
material_ingles = float(input("Ingresa tu calificación de Ingles:"))

suma = material_español + material_matematicas + material_economia + material_programacion + material_ingles

promedio = suma / 5

print("Tu promedio es de :", promedio)