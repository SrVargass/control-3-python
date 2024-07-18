def es_binario(var):
    for x in var:
        if x != "0" and x!="1":
            return False
    return True

print(es_binario("101010")) 
print(es_binario("HOLA"))  
print(es_binario("CHAO"))
print(es_binario("010101"))

