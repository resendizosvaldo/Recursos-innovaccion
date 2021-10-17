
def validacionEdad() :
    #IMPRIMIR TU NOMBRE
    nombre = input("Introduce tu nombre: ")
    #CONCATENACION - PONER UNA VARIABLE JUNTO CON UN TEXTO PLANO
    print(f"Hola {nombre}")
    print("Hola {}".format(nombre))
    print("Hola " + nombre)

    #ENTERO
    edad = input("Ahora introduce tu edad: ")
    #FLOTANTE DECIMALES
    estatura = 1.75
    #CONVERTIR FLOTANTE
    edadString = str(edad)#Palabra que contiene el 2 y el 5 (25)
    booleanos = False #True

    print(type(edad))
    print(type(edadString))

    #transformar string a entero
    edad = int(edad)

    #ESTRUCTURA DE CONTROL IF
    if edad >= 18 and edad < 100: #Si tu edad es mayor o igual a 18 o menor a 100
        print("Hola {} pasale por tu tonayan".format(nombre)) #Hará esto
    elif edad >= 100 : #Si no, entonces ¿Edad es mayor  o igual a 100?
        print("¿Acaso eres chabelo?")#Hará esto
    elif edad <= 0 :
        print("Aún ni naces mi chavo, te la bañaste")
    else :
        print("Estás chavo mi buen")
    #ESTRUCTURA DE CONTROL FOR

while True :
    validacionEdad()
