# VIDEO - Fechas con Python

# Para que nosotros podamos trabajar con fechas utilizando Python haremos uso de la librería datetime. En esta ocasión listaremos un par de ejemplos que pueden ayudarte a comprender de una mejor manera dicha librería.

# OBTENER LA FECHA ACTUAL.

#Es necesario importar las depencendias necesarias
from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

print(today)
print(now)

# ATRIBUTOS

# Una vez obtengamos la fecha actual podremos obtener el día, mes, año, hora, minutos, segundos de esta.

#Date
print("El día actual es {}".format(today.day))
print("El mes actual es {}".format(today.month))
print("El año actual es {}".format(today.year))


#Datetime
print("El día actual es {}".format(now.day))
print("El mes actual es {}".format(now.month))
print("El año actual es {}".format(now.year))

print("La hora actual es {}".format(now.hour))
print("El minuto actual es {}".format(now.minute))
print("El segundo actual es {}".format(now.second))

# NUEVA FECHA

# Si nosotros así lo deseamos podemos trabajar con una fecha en particular.

new_date = datetime(2019, 2, 28, 10, 15, 00, 00000)

# Los argumentos serán: Año, Mes, Día, Hora, Minutos, Segundos, Milisegundos

# OPERACIONES

# En ocasiones tendremos la necesidad de realizar ciertas operaciones con fechas, ya sea agregar días, restar años o simplemente realizar comparaciones. Con Python todas estas operaciones podremos realizarlas sin ningún problema.

from datetime import datetime
from datetime import timedelta

#Sumar dos días a la fecha actual
now = datetime.now()
new_date = now + timedelta(days=2)
print(new_date)

#Comparación
if now < new_date:
    print("La fecha actual es menor que la nueva fecha")

# FORMATO DE FECHAS

# Aunque las fechas en Python ya poseen un formato legible para los humanos, en ocasiones necesitaremos ser más explícitos para no dejar espacio a la ambiguuedad, para ello, haremos uso del método strftme.

now = datetime.now()
format = now.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
print(format)

# %d Día
# %m Mes
# %Y Año
# %H Hora
# %M Minutos
# %S segundos

# Algo que en lo particular me gusta hacer es definir una función que me permita obtener un formato mucho más amigable.

from datetime import datetime

def current_date_format(date):
    months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    day = date.day
    month = months[date.month - 1]
    year = date.year
    messsage = "{} de {} del {}".format(day, month, year)

    return messsage

now = datetime.now()
print(current_date_format(now))