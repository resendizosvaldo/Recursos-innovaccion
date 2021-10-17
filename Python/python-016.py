dic1 = {'Lorca':'Escritor', 'Goya':'Pintor'} # declara diccionario 
print(dic1) # {'Goya': 'Pintor', 'Lorca': 'Escritor'}
dic2 = dict((('mesa',5), ('silla',10))) # declara a partir de tupla
print(dic2)
dic3 = dict(ALM=5, CAD=10) # declara a partir de cadenas simples 
print(dic3)
dic4 = dict([(z, z**2) for z in (1, 2, 3)]) # declara a partir patrón
print(dic4)  # muestra {1: 1, 2: 4, 3: 9}
print(dic1['Lorca'])  # escritor, acceso a un valor por clave
print(dic1.get('Gala', 'no existe'))  # acceso a un valor por clave
if 'Lorca' in dic1: print('está')  # comprueba si existe una clave
print(dic1.items())  # obtiene una lista de tuplas clave:valor
print(dic1.keys())  # obtiene una lista de las claves
print(dic1.values())  # obtiene una lista de los valores
dic1['Lorca'] = 'Poeta'  # añade un nuevo par clave:valor
print(dic1)
dic1['Amenabar'] = 'Cineasta'  # añade un nuevo par clave:valor
print(dic1)
dic1.update({'Carreras' : 'Tenor'})  # añadir con update()
print(dic1)
del dic1['Amenabar']  # borra un par clave:valor 
print(dic1.pop('Amenabar', 'no está'))  # borra par clave:valor
