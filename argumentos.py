def funcion1(arg1:int,arg2:int)->None:
    print(f"argumento1:{arg1}, argumento2:{arg2}")

# una funcion con valores por defecto
def funcion2(arg1:int=0,arg2:int=0)->None:
    print(f"funcion2, argumento1:{arg1}, argumento2:{arg2}")

# para que me sirve un wargs?
# sirve para especificar una funcion con una cantidad indeterminada de argumentos posicionales.
def funcion3(*args)->None:   # * indica un "wargs"
    print(args)


funcion1(20,30)  # argumento1:20, argumento2:30 (llamada argumento posicional)
funcion1(arg1=20,arg2=30)  # argumento1:20, argumento2:30
funcion1(arg2=30,arg1=20)  # no importa el orden

funcion2(arg2=222)  # llame a la funcion, y arg1 toma el valor por defecto (0)

funcion3(20,30,40)

