import math

print("este programa  lee un conjunto de datos calcula y despliega la media y la desviacion")
print("")

# menu


def menu():

    dato = leer_datos()
    media = Media(dato)
    desvi = Desviacion(dato, media)
    mostrar(dato, media, desvi)


# lee todos los datos ingrasados por el usuario
lista = []


def leer_datos():

    print("ingrese el numero de datos que desea ingresar")
    n = input()
    n = int(n)
    while n <= 1:
        print("ingrese el numero de datos que desea ingresar")
        n = input()
        n = int(n)

    for k in range(1, n+1):
        print("ingrese el dato", k, ")")
        dato = input()
        dato = int(dato)

        lista.append(dato)

    return lista

# calcula la media de los datos ingresados


def Media(dato):

    prom = sum(dato)/len(dato)

    return prom

# calcula la desviacion de los datos ingrasados por el usuario


def Desviacion(dato, media):

    sigma = 0.0

    for elemento in lista:
        sigma += (elemento-media)**2

    desvi = math.sqrt(sigma/(len(dato)-1))

    return desvi

# muestra el resultado optenido


def mostrar(dato, media, desvi):

    print("resultados")

    for k in range(len(dato)):
        print(k+1, ")  ", dato[k])

    print("media:  ", format(media))
    print("desviacion:   ", format(desvi))


continuar = "si"

while continuar == "si" or continuar == "SI":
    menu()
    continuar = input("desea hacer algo mas  (si/no):  ")


print("gracias por usar este programa")
