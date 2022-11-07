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


ve=Vehiculo("aa-22-33","subaru","modelo",33)

v2=Vehiculo("aa-4423","subaru","gt-2000",333)




