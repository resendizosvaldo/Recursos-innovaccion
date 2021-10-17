cadena1 = "Cuba"
cadena2 = "Costa Rica"
print(cadena1.isalpha())   # True
print(cadena1.isalnum())   # True
print(cadena1.isdecimal())   # False
print(cadena1.isspace())   # False
print(cadena2.istitle())   # True
if cadena1.isalpha():
    print("Todos los caracteres que contiene son alfabéticos")

