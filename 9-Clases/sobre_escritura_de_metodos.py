# VIDEO - Sobre escritura de métodos

# -Se coloca el método a sobre escribir y poner sus funcionalidades

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

    def dormir(self):
        print(self.nombre, "Esta durmiendo")
        Animal.dormir(self)
        print("No molestar")

firulais = Perro("Firulais")
firulais.dormir()
