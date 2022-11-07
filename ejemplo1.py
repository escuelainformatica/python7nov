# Chile-express

# diccionario:
encomienda={
    "alto":2,
    "ancho":2,
    "largo":2,
    "peso":2.3,
    "origen":"Santiago",
    "destino":"punta arenas"
}
# clase
class ClaseEncomienda():
    # campos:
    alto=0
    ancho=0
    largo=2
    peso=0.0
    origen=""
    destino=""

    def __init__(self):
        print("hola mundo")


encomienda2=ClaseEncomienda()   # encomienda2 es un objeto del tipo ClaseEncomienda (instancia)
encomienda2.alto=2
encomienda2.ancho=2
encomienda2.largo=2
encomienda2.peso=2.3
encomienda2.origen="Santiago"
encomienda2.destino="punta arenas"

print(encomienda)
print(encomienda2)





