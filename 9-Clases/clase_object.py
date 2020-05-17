# VIDEO - Clase Object

# -Todas las clases que nosotros creamos estarán heredando a una clase común

class Gato():
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre

class Pato(object):
    def __init__(self, nombre):
        self.nombre = nombre

gato = Gato("Bigotes")
pato = Pato("Lucas")

print(gato.__dict__)
print(pato.__dict__)