cadena1 = 'Python'  # Declara cadena con 'Python'
cadena2 = 'Lenguaje ' + cadena1.upper()  # Lenguaje PYTHON
cadena3 = 'Lenguaje ' 'Python'  # Lenguaje Python
cadena3 = cadena1.lower() * 3  # pythonpythonpython 
cadena4 = "Python para impacientes"
print(cadena4.title())  # Python Para Impacientes 

# Uso de paréntesis en expresiones
total1 = ((24 - 10 + 2.3) * 4.3 / 2.1) ** 2

print(total1)  # 1113.9700907
print(type(cadena1))  # type str=""
print(type(total1))  # type float=""
del cadena1  # Borra la variable de memoria
print(cadena1)  # Genera un error porque no existe

