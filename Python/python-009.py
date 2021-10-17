# Evaluar variables por tipo de dato que contienen

var1 = "Python 3"
var2 = 3
var3 = 3.14
var4 = True
var5 = [1, 2, 3]
var6 = ('a', 'b', 'c')
var7 = {'a':1, 'b':2, 'c':3}

if type(var1) is str:
    print("'var1' es una cadena")

if type(var2) is int:
    print("'var2' es una número entero")

if type(var3) is float:
    print("'var3' es un número con decimales")

if type(var4) is bool:
    print("'var4' es un booleano")

if type(var4):
    print("'var4' es un booleano")

if type(var5) is list:
    print("'var5' es una lista")

if type(var6) is tuple:
    print("'var6' es una tupla")

if type(var7) is dict:
    print("'var7' es un diccionario")

# Evaluar si cadena, lista o diccionario están vacíos

var1 = ""
var2 = []
var3 = {}

if not var1:
    print("Cadena vacía")

if not var2:
    print("Lista sin elementos")
    
if not var3:
    print("Diccionario sin claves/valores")

# Evaluar si una variable no tiene ningún valor

var4 = None
if not var4:
    print("No tiene ningún valor")
