def digitos(num):
    caracter = str(num)
    digito = []
    for x in caracter:
        digito.append(x)
    res = len(digito)
    return res

num = int(input("Ingrese un número: "))
cantidad= digitos(num)
print(f"La cantidad de dígitos que tiene {num} es {cantidad}")
