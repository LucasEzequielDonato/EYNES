""" Crear una matriz de 5x5 randomizada con números enteros, encontrar secuencia de 4
números consecutivos horizontal o vertical y si se encuentra mostrar la posición inicial y
final. """

from random import randint

""" Se importo esto para generar los numeros random """


def crear_matriz():
    m = [[randint(1, 100) for j in range(5)] for i in range(5)]
    """ Aqui creo la matriz con numeros random """
    i = 0
    while i < 5:
        """ Aqui recorro cada fila de la matriz """
        if (
            m[i][0] == m[i][1]
            and m[i][0] == m[i][2]
            and m[i][0] == m[i][3]
            and m[i][0] != m[i][4]
        ):
            print(
                "Se encontro secuencia consecutiva vertical, inicia en la fila "
                + str((i + 1))
                + " celda "
                + str(1)
                + " y termina en la fila "
                + str((i + 1))
                + " celda "
                + str(4)
            )
            """ Se le agrega 1 a la ubicacion ya que las personas cuentan desde el 1 y no desde el 0 """
        elif (
            m[i][1] != m[i][0]
            and m[i][1] == m[i][2]
            and m[i][1] == m[i][3]
            and m[i][1] == m[i][4]
        ):
            """ Aqui verifico si hay secuencialidad vertical """
            print(
                "Se encontro secuencia consecutiva vertical, inicia en la fila "
                + str((i + 1))
                + " celda "
                + str(2)
                + " y termina en la fila "
                + str((i + 1))
                + " celda "
                + str(5)
            )
            """ Se le agrega 1 a la ubicacion ya que las personas cuentan desde el 1 y no desde el 0 """
        if (
            m[0][i] == m[1][i]
            and m[0][i] == m[2][i]
            and m[0][i] == m[3][i]
            and m[0][i] != m[4][i]
        ):
            print(
                "Se encontro secuencia consecutiva horizontal, inicia en la fila "
                + str(1)
                + " celda "
                + str((i + 1))
                + " y termina en la fila "
                + str(4)
                + " celda "
                + str((i + 1))
            )
            """ Se le agrega 1 a la ubicacion ya que las personas cuentan desde el 1 y no desde el 0 """
        elif (
            m[1][i] != m[0][i]
            and m[1][i] == m[2][i]
            and m[1][i] == m[3][i]
            and m[1][i] == m[4][i]
        ):
            """ Aqui verifico si hay secuencialidad horizontal """
            print(
                "Se encontro secuencia consecutiva horizontal, inicia en la fila "
                + str(2)
                + " celda "
                + str((i + 1))
                + " y termina en la fila "
                + str(5)
                + " celda "
                + str((i + 1))
            )
            """ Se le agrega 1 a la ubicacion ya que las personas cuentan desde el 1 y no desde el 0 """
        i += 1


if __name__ == "__main__":
    crear_matriz()
    """ Aqui invoco la funcion para probar la funcionalidad de la misma """
    """ Si no muestra nada es que no hubo secuencia """