# VIDEO - Herencia

# -Se puede reutilizar código
# -Para poder heredar de otra clase se colocan (NombreDeLaClase) a la que se quiere heredar

class Animal:
    def comer(self):
        print("comiendo")

    def dormir(self):
        print("durmiendo")

class Perro(Animal): 
    def __init__(self, nombre):
        self.nombre = nombre

    def ladrar(self):
        print("ladrando")

class Gato(Animal):
    def ronroneo(self):
        print("ronroneo")

firulais = Perro("Firulais")
firulais.ladrar()
firulais.comer()
firulais.dormir()

bola_nieve = Gato()
bola_nieve.comer()
bola_nieve.dormir()
bola_nieve.ronroneo()