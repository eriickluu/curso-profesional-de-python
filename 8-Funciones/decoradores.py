# VIDEO - Decoradores

# -Para tener un decorador por lo menos se necesitan 3 funciones
# -Para decorar a una función se utiliza "@ y el nombre de la función"
# -a(b) -> c

def decorador(funcion):
    
    def nueva_funcion():
        print("podemos agregar código antes")
        funcion()
        print("Agregar código después")

    return nueva_funcion

@decorador
def funcion_a_decorar():
    print("Esta en una funcion a decorar")

funcion_a_decorar()