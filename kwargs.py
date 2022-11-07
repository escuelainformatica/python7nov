# kwargs

def mostrar(**kwargs):
    # kwargs se especifica con dos asterisco, es igual que el wargs, pero con argumentos con nombre
    # kwargs transforma los argumentos en un diccionario.
    print(kwargs)


mostrar(primer="hola",segundo="mundo") # {'primer': 'hola', 'segundo': 'mundo'}



