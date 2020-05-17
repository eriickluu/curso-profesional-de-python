# VIDEO - Ciclo while

# -El código del else se ejecutará cuando la condición ya no se cumpla

numero = 123456789
contador = 0

while numero >= 1:
   contador+=1 
   numero = numero / 10
else:
   print('la cantidad de dígitos de número es', contador)