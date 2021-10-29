""" Hacer una función que genere una lista de diccionarios que contengan id y edad, donde
edad sea un número aleatorio entre 1 y 100 y la longitud de la lista sea de 10
elementos. retornar la lista. 
Hacer otra función que reciba lo generado en la primer función y ordenarlo de mayor a
menor. Printear el id de la persona más joven y más vieja. Devolver la lista ordenada. """

""" Importo esto para generar numeros random """
import random


def crear_lista():
    """ Esta funcion genera la lista con los 10 diccionarios """
    i = 1
    lista = []
    while i <= 10:
        diccionario = {"id": i, "edad": random.randint(1, 100)}
        lista.append(diccionario)
        i += 1
    return lista


def ordenar(lista):
    """ Esta funcion ordena la lista y muestra el resultado final """
    for recorrido in range(1, len(lista)):
        for posicion in range(len(lista) - recorrido):
            if lista[posicion]["edad"] > lista[posicion + 1]["edad"]:
                cambio = lista[posicion]
                lista[posicion] = lista[posicion + 1]
                lista[posicion + 1] = cambio
    print(
        "La persona más joven es la del id: "
        + str(lista[0]["id"])
        + " que tiene "
        + str(lista[0]["edad"])
        + " años"
    )
    print(
        "La persona más vieja es la del id: "
        + str(lista[9]["id"])
        + " que tiene "
        + str(lista[9]["edad"])
        + " años"
    )
    return lista


if __name__ == "__main__":
    print(ordenar(crear_lista()))
    """ Aqui invoco la funcion para probar la funcionalidad de la misma, dentro de un print para visualizar lo que retorna la funcion """