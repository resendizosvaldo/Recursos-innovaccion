edad=15

# Evaluar distintos valores numéricos

if edad <= 12:  # se evalúa la primera condición... 
    precio = 2  # y si edad es menor igual que 12, precio = 2
elif 13 <= edad <= 18:  # en caso contrario se evalúa...
    precio = 3  # si edad está entre 13 y 18, precio = 3
else:  # en cualquier otro caso...
    precio = 4  # precio = 4
print('A Pagar: $' + str(precio))  # Muestra importe

# Evaluar en una sola línea

print('par' if edad % 2 == 0 else 'impar')
