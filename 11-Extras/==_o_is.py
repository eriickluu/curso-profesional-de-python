# En el vídeo de Operadores relacionales y lógicos mencianamos que es posible conocer si dos valores enteros son iguales mediante 
# el uso de == y la palabra reservada is; Sin embargo, ahora que ya contamos con más conocimiento del que teníamos 
# en ese vídeo es importante conocer cuando usaremos == y cuando usaremos is. Veamos.

# Si ejecutamos la siguiente línea de código obtendremos como resultado True.

[1,2,3] == [1,2,3]

# Eso de deben a que ambas listas son iguales. Ahora, ¿Qué pasa si reemplazamos == por is?

[1,2,3] is [1,2,3]

# En este casa obtenemos False; Esto se debe a que con == compararemos que dos valores sean iguales y con is compareremos que dos objetos sean iguales,
#  cosas completamente diferentes.

# Veamos un par de ejemplos para que nos quede más en claro.

a = [1,2,3]
b = [1,2,3]

# A la primera lista la llamaremos a y a la segunda b.

# Si imprimimos el id de cada objeto, observaremos que son valores completamente diferentes, con lo cual concluimos que son dos objetos diferentes.

print(id(a))
print(id(b))

# Si ejecutamos.

a = [1, 2, 3]
b = a

a is b 

# Obtendremos cómo resultado True, debido a que a y b son el mismo objeto.

# En conclusión == nos permite saber si dos objetos son iguales, mientras que is nos permite conocer si cuando los objetos son los mismos.