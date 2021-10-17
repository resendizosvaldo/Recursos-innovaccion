#USO DE LA POKE API
#API https://pokeapi.co/api/v2/pokemon/
#IMPORTAMOS LIBRERIAS
import requests
import matplotlib.pyplot as plt
import matplotlib.image as img

#Solicitamos el nombre del pokemon
pokemon = input("Introduce el nombre del Pokemon: ")

#CONCATENAMOS LA URL DE LA API CON EL NOMBRE DEL POKEMON EXPLICADO DE OTRA MANERA... UNIMOS LA URL CON EL NOMBRE INTRODUCIDO
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
res = requests.get(url)

if res.status_code != 200 :
    print("Pokemon no encontrado")
    exit()

imagen = img.imread(res.json()['sprites']['front_default'])
plt.title(res.json()['name'])
imgplot = plt.imshow(imagen)
plt.show()