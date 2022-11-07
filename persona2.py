class Persona():
    # campos: (voluntarios)
    nombre:""
    apellido:""

    def __init__(self,arg_nombre,arg_apellido):  # iniciador
        self.nombre=arg_nombre
        self.apellido=arg_apellido


john=Persona("john","doe")

print(john)

