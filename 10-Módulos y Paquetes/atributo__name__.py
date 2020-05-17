# VIDEO - Atributo __name__

# -El archivo principal siempre tendrá por nombre __main__

import calculadora

print(calculadora.__name__)
print(__name__)

if __name__ == '__main__':
    print("Soy el archivo principal")
else:
    print("Estoy siendo usado como modulo")