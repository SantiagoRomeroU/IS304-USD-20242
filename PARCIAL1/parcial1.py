// escriba un programa en python que permita clasificar triaungulos (isoceles,escaleno,equilatero, rectangulo) a partir de 3 datos flotantes o doubles ingresados desde el teclado.
// definir y utilizar al menos una referencia de herencia que incluya encapsulamiento
// el programa debe repetirse continuamente hasta que 1 de los supuestos triangulos no lo sea
class Triangulo:
    # Constructor
    def __init__(self, lado1, lado2, lado3):
        # Se instancian las variables privadas para encapsularlas
        self._lado1 = lado1
        self._lado2 = lado2
        self._lado3 = lado3

    def clasificar(self):
        if self._lado1 == self._lado2 == self._lado3:
            return "Equilátero"
        elif self._lado1 == self._lado2 or self._lado2 == self._lado3 or self._lado1 == self._lado3:
            return "Isósceles"
        else:
            return "Escaleno"

# La clase TrianguloRectangulo hereda de Triangulo
class TrianguloRectangulo(Triangulo):
    def es_rectangulo(self):
        lados = sorted([self._lado1, self._lado2, self._lado3])
        return lados[0]**2 + lados[1]**2 == lados[2]**2

def es_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1

# Bucle que repite el programa hasta que se ingresen datos que no formen un triángulo
while True:
    try:
        lado1 = float(input("Ingresa el lado 1: "))
        lado2 = float(input("Ingresa el lado 2: "))
        lado3 = float(input("Ingresa el lado 3: "))

        if not es_triangulo(lado1, lado2, lado3):
            print("Los lados ingresados no forman un triángulo. Fin del programa.")
            break

        triangulo = TrianguloRectangulo(lado1, lado2, lado3)

        tipo = triangulo.clasificar()
        es_rectangulo = triangulo.es_rectangulo()

        print(f"El triángulo es: {tipo}")
        if es_rectangulo:
            print("Además, es un triángulo rectángulo.")

    except ValueError:
        print("Por favor, ingresa valores numéricos válidos para los lados del triángulo.")
