# VIDEO - Métodos de clase

# -Los métodos de clase obligatoriamente tiene que llevar un parámetro y por buena practica se le llama "cls"
# -Los métodos de clase comúnmente se utilizan cuando tienes que usar variables de clase
# -Comúnmente se usan métodos de clase cuando se necesita usar variables de clase

class Circulo:

    pi = 3.1416

    @classmethod
    def area(cls, radio):
        return cls.pi * radio**2

resultado = Circulo.area(10)
print(resultado)