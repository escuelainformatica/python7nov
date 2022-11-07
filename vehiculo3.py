class Vehiculo():
    patente=""
    marca=""
    modelo=""
    precio=0

    def __init__(self,patente,marca,modelo,precio):
        self.patente=patente
        self.marca=marca
        self.modelo=modelo
        self.precio=precio


ve=Vehiculo(patente="aa-2233",marca="Subaru",modelo="gt-2022",precio=2000)




