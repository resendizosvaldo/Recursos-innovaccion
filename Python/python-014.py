lista1 = ['uno', 2, True]  # declara una lista heterogénea
lista2 = [1, 2, 3, 4, 5]  # declara lista numérica (homogénea)
lista3 = ['nombre', ['ap1', 'ap2']]  # declara lista dentro de otra
lista4 = [54,45,44,22,0,2,99]  # declara una lista numérica
print(lista1)  # ['uno', 2, True], muestra toda la lista
print(lista1[0])  # uno, muestra el primer elemento de la lista
print(lista2[-1])  # 5, muestra el último elemento de la lista
print(lista3[1][0])  # calle, primer elemento de la lista anidada
print(lista2[0:3:1])  # [1,2,3], responde al patrón inicio:fin:paso
print(lista2[::-1])  # devuelve la lista ordenada al revés
lista1[2] = False  # cambia el valor de un elemento de la lista
print(lista1)
lista2[-2] = lista2[-2] + 1  # 4+1 → 5 – cambia valor de elemento
print(lista2)
lista2.pop(0)  # borra elemento indicado o último si no indica
print(lista2)
lista1.remove('uno')  # borra el primer elemento que coincida
print(lista1)
del lista2[1]  # borra el segundo elemento (por índice)  
print(lista2)
lista2 = lista2 + [6]  # añade elemento al final de la lista
print(lista2)
lista2.append(7)  # añade un elemento al final con append()
print(lista2)
lista2.extend([8, 9])  # extiende lista con otra por el final
print(lista2)
lista1.insert(1, 'dos')  # inserta nuevo elemento en posición
print(lista1)
del lista2[0:3]  # borra los elementos desde:hasta
print(lista2)
lista2[:] = []  # borra todos los elementos de la lista 
print(lista2)
print(lista1.count(2))  # cuenta el nº de veces que aparece 2
print(lista1.index("dos"))  # busca posición que ocupa elemento
lista4.sort()  # ordena la lista
print(lista4)
lista4.sort(reverse=True)  # ordena la lista en orden inverso
print(lista4)
lista5 = sorted(lista4)  # ordena lista destino 
print(lista5)
tupla1 = (1, 2, 3)  # declara tupla (se usan paréntesis)...
tupla2 = 1, 2, 3  # ...aunque pueden declararse sin paréntesis
print(tupla2)
tupla3 = (100,)  # con un elemento hay terminar con “,”
print(tupla3)
tupla4 = tupla1, 4, 5, 6  # anida tuplas
print(tupla4)
tupla5 = ()  # declara una tupla vacía
print(tupla2[0:2])  # (1, 2, 3), accede a los valores desde:hasta
