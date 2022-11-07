# python7nov

## tipos de argumentos

```python
def funcion1(arg1,arg2):   # argumentos requeridos
    pass
def funcion2(arg1,arg2=0):  # con un argumento opcional 
    pass
def funcion3(*wargs):  # con cero,uno o mas argumentos posicionales
    pass
def funcion4(**kwargs):  # con cero, uno o mas argumentos con nombre
    pass

funcion1(1,2)  # argumentos posicionales
funcion1(arg1=1,arg2=2)  # argumentos con nombre
funcion2(1) # el segundo argumento es opcional
funcion3(1,2,3,4,5)  # argumentos posicionales
funcion4(arg1=1,arg2=2,arg3=3,arg4=4)   # argumentos con nombre
```

## clases

```python
class NombreClase():
    # (campos son opcional)
    campo1=""
    campo2=0
    
    # (iniciador o constructor, tambien es opcional)
    def __init__(self,campo1="11",campo2=999):
        self.campo1=campo1
        self.campo2=campo2
        
    # (metodo o funcion dentro de la clase
    def metodo(self):
        print(f"campo1:{self.campo1},campo2:{self.campo2}")
```

## objeto
Un objeto es una variable definida por una clase

```python
objeto1=NombreClase("aaaa",555) # crear un objeto del tipo NombreClase
objeto1.metodo()  # llamar a un metodo dentro de la clase
objeto1.campo1="2222"  # asignar un valor a un campo
```
