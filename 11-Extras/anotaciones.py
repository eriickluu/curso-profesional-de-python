# VIDEO - Anotaciones

# -Las anotaciones son únicamente para carácter informativo

def saludo(nombre : str) -> None:
    print("Hola " + nombre)

def suma(num1 : int, num2 : int = 100) -> int:
    return num1 + num2

nombre = "Erick"
saludo(nombre)

print(suma(10))