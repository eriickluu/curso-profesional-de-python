# VIDEO - Herencia múltiple

# -Una clase puede heredar más de una solo los separas por una ,
# -Las clases de las cuales sé está heredando se deben encontrar en la parte de arriba del script

class Animal:
    def comer(self):
        print("comiendo")

    def dormir(self):
        print("durmiendo")

    def comun(self):
        print("Este es un método de Animal")

class Mascota:
    def fecha_adopcion(self, fecha):
        self.fecha_de_adopcion = fecha 

    def comun(self):
        print("Este es un método de Mascota")

class Perro(Animal, Mascota): 
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("ladrando")

    def comun(self):
        print("Este es un método de Perro")

class Gato(Animal):
    def ronroneo(self):
        print("ronroneo")

firulais = Perro("Firulais")
firulais.fecha_adopcion("Hoy")
print(firulais.fecha_de_adopcion)

firulais.comun()