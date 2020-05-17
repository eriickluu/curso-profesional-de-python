# VIDEO - Búsqueda de cadenas

# -

mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"

# Buscar un veces que un texto se encuentra dentro de un string
resultado = mensaje.count("e")

# Saber si un texto se encuentra en un string
resultado = "texto" in mensaje

# Saber la posición en la que se encuentra el texto en nuestro string
# resultado = mensaje.find("texto")

# Saber si se inicia con un texto en especifico 
resultado = mensaje.startswith("Este")

# Saber si se termina con un texto en especifico 
resultado = mensaje.endswith("e")

print(resultado)