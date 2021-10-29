""" Escribir una clase en python llamada círculo que contenga un radio, con un método que
devuelva el área y otro que devuelva el perímetro del círculo.
Si se instancia la clase con radio <= 0 mostrar una excepción indicando un error amigable al
usuario e impidiendo la instanciación.
Si printeamos el objeto creado debe mostrarse una representación amigable.
El objeto debe tener su atributo radio modificable, si se le intenta setear un valor <= 0
mostrar un error y no permitir modificación.
Permitir la multiplicación del circulo: Circulo * n debe devolver un nuevo objeto con el radio
multiplicado por n. No permitir la multiplicación por números <= 0 """

from math import pi


class Circulo:
    def __init__(self, radio):
        if radio <= 0:
            raise Exception(
                "Ingreso un numero menor o igual a 0, no se puede instanciar el circulo."
            )
        else:
            self.radio = radio

    def __repr__(self):
        return (
            "Soy tu circulo\nMi radio es "
            + str(self.radio)
            + " mi area es "
            + str(self.devolver_area())
            + " y mi perimetro es "
            + str(self.devolver_perimetro())
        )

    def devolver_area(self):
        return pi * self.radio ** 2

    def devolver_perimetro(self):
        return 2 * self.radio * pi

    def modificar_radio(self):
        print("Ingrese un nuevo radio para su circulo (Mayor a 0):")
        radio = int(input())
        if radio <= 0:
            print(
                "Ingreso un numero menor o igual a 0, no es un numero valido, operacion no realizada."
            )
        else:
            self.radio = radio

    def multiplicar_radio(self):
        print("Ingrese un numero que multiplicara el radio (Mayor a 0):")
        multiplicador = int(input())
        if multiplicador <= 0:
            print(
                "Ingreso un numero menor o igual a 0, no es un numero valido, operacion no realizada."
            )
            return self
        else:
            nuevo_circulo = Circulo(self.radio * multiplicador)
            """ Aqui al realizarce la multiplicacion de forma correcta se genera un nuevo circulo """
            return nuevo_circulo


def inicio_ejercicio():
    """ Esta funcion es para comenzar el ejercicio """
    print("Ingrese el radio que quisiera que tenga su circulo (Mayor a 0):")
    radio = int(input())
    circulo_panel(Circulo(radio))


def circulo_panel(circulo):
    """ Esta funcion sirve de panel para el usuario """
    print(circulo)
    print("Si quiere cambiar el radio del circulo ingrese 1")
    print("Si quiere multiplicar el radio ingrese 2 (Creara un nuevo circulo)")
    opcion = int(input())
    if opcion == 1:
        circulo.modificar_radio()
        circulo_panel(circulo)
    elif opcion == 2:
        circulo_panel(circulo.multiplicar_radio())
    else:
        print("La opcion no es una opcion valida")
        circulo_panel(circulo)


if __name__ == "__main__":
    inicio_ejercicio()
    """ Aqui invoco la funcion para probar la funcionalidad de la misma """