# VIDEO - Tipos de atributos

# -Se pueden tener variables de instancia y de clase en las clases

class Circulo:
    pi = 3.1416 #Es una variable de clase

    def __init__(self, radio):
        self.radio = radio #Es una variable de instancia

circulo_a = Circulo(10)
circulo_b = Circulo(20)

circulo_b.radio = 100

print(circulo_a.radio)
print(circulo_b.radio)

# Para acceder a las variables de clase no ocupas hacer instancia
print(circulo_a.pi)
print(circulo_b.pi)