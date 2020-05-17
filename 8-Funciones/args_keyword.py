# VIDEO - Args keyword

# -Siempre que se utilice el * en un parámetro este tenga por nombre "args" 
# -Siempre que se utilice el ** en un parámetro este tenga por nombre "kwargs" 
# -El uso de ** agrupa los argumentos en un diccionario

# def suma(*args):
#     total = 0
    
#     # print(args)
#     for valor in args:
#         total += valor
#     return total

# resultado = suma(10, 20, 30, 40, 50, 60)
# print(resultado)

def suma(parametro_requerido, *args):
    total = 0
    print(parametro_requerido)
    for valor in args:
        total += valor
    return total

def usuarios_autenticados(**kwargs):
    print(kwargs)

resultado = suma("Este es un argumento requerido", 10, 20, 30, 40, 50, 60)
print(resultado)

usuarios_autenticados(codi=True, facilito=False)

def combinacion(requerido, *args, **kwargs):
    print(requerido)
    print(args)
    print(kwargs)

combinacion("Valor requerido", 10, 20, valor_uno=True, valor_dos=False)