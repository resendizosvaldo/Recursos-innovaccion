# Ejemplo de bucle con 'break'

contador = 0
limite = 5
while contador < 11:  # el bucle termina cuando contador=10 
    if contador == limite:  # o cuando alcance el valor limite 
        break
    else:
        contador += 1  # contador se incrementa en 1
        print(contador, limite)

# Ejemplo de bucle con 'continue' y 'break'

x=0
y=0
limite = 5
while True:
    y+=1
    if y!=limite:
        x+=y
    else:
        break
    if y!=3:
        continue
    print(x,y)
