# VIDEO - Desempaquetado de tuplas

# En ciertas ocasiones tendremos la necesidad de obtener algunos elementos de nuestras tuplas, por ejemplo, teniendo la siguiente tupla.

tupla = (10, 20, 30, 40, 50)

# Necesito obtener el primero, el segundo y el último elemento; Para lograr esto tendremos un par de opciones; trabajando con índices y sin ellos. Veamos.

# Si trabajamos con índices podemos hacerlo lo siguiente.

primero = tupla[0]
segundo = tupla[1]
ultimo = tupla[-1]

# o simplemente podemos reducir las líneas de código y dejarlo en una sola.

primero, segundo, ultimo = tupla[0], tupla[1], tupla[-1]

# La segunda opción es dejar de trabajar con las los índices y utilizar el guión bajo _.

primero, segundo, _, _, ultimo = tupla

# Como observamos he colocado dos guiones bajos que hacen referencia a el número 30 y el número 40, valores que no necesitamos, por en de, no necesito almacenarlos en alguna variable; simplemente los ignoramos.

# Ahora, que pasa si tengo una tupla mucho más grande y nuevamente necesito obtener esos tres elementos (el primero, el segundo y el último).

tupla = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400)

# Lo que podemos hacer es utilizar el guión bajo _ junto con el asterisco * y aplicar lo que hemos visto anteriormente.

primero, segundo, *_, ultimo = tupla

# De esta forma podemos trabajar de una forma más eficiente con las tuplas.