
def sumar(*valores):
    """
    esta funcion permite sumar valores
    :param valores: deben ser valores numericos
    :return: la suma
    """
    total=0
    for valor in valores:
        total=total+valor
    return total

print(sumar(1,2,3,4,5))


