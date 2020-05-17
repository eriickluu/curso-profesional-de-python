# VIDEO - Métodos

# -Los métodos son las acciones que hacen los objetos
# -Todos los métodos tendrán que recibir un parámetro, ese parámetro sera "self"

class Usuario():
 
    # def saluda(self, nombre):
    #     print("hola soy un usuario " + nombre)

    def saluda(self, nombre):
        return "hola soy un usuario " + nombre

codi = Usuario()
facilito = Usuario()

print(codi.saluda("codi"))
print(facilito.saluda("facilito"))