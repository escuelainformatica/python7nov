class ClaseEncomienda():
    # campos: (no son necesarios)
    alto=0
    ancho=0
    largo=2
    peso=0.0
    origen=""
    destino=""

    # iniciador (constructor), para inicializar el objeto cuando se crea.
    def __init__(self,alto=0,ancho=0,largo=0,peso=0.0,origen="",destino=""):
        self.alto=alto
        self.ancho = ancho
        self.largo = largo
        self.peso = peso
        self.origen = origen
        self.destino = destino

    # metodos o funciones:
    def volumen(self) -> int:
        return self.alto * self.ancho * self.largo

    def costo_envio(self)->float:
        return self.volumen()*self.peso*10.5

enc1=ClaseEncomienda(alto=2,ancho=2,largo=2,peso=2)

print(enc1.volumen())
print(enc1.costo_envio())

