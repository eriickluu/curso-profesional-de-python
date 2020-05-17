# VIDEO - Atributos

# -Se pueden declarar atributos dentro y fuera de la clase
# -Es buena practica inicializar los valores desde el método "__init__"

class Usuario():

    def __init__(self, username='', correo='', nombre=''):
        self.username = username
        self.correo = correo
        self.nombre = nombre

    def saluda(self):
        return "hola soy un usuario " + self.nombre

    def mostrar_username(self):
        print(self.username)
    
    def mostrar_nombre(self):
        print(self.nombre)

    # def crear_nombre(self, nombre):
    #     self.nombre = nombre

codi = Usuario("codi", "codi@codigofacilito.com", "Codigo")
# codi.username = 'codi'
# codi.correo = 'codi@gmail.com'

facilito = Usuario()
# facilito.username = 'facilito'
# facilito.correo = 'facilito@gmail.com'

codi.mostrar_username()
facilito.mostrar_username()

# codi.crear_nombre("erick")
# codi.mostrar_nombre()

resultado = codi.saluda()
print(resultado)