# Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
# La función recibirá el mes y el año y retornará verdadero o falso.


import datetime

def metodo_main():
    ano = int(input("Ingrese el año : "))
    mes = int(input("Ingrese el mes : "))

    comprobador = Viernes13(ano, mes)

    if comprobador.es_viernes_13():
        print(f"VERDADERO")
    else:
        print(f"FALSO")


class Viernes13:
    # Constructor de la clase
    def __init__(self, ano, mes):
        self.ano = ano
        self.mes = mes

    # se valida si el dia 13 cae viernes
    def es_viernes_13(self):
        if 1 <= self.mes <= 12 and 1 <= self.ano <= 9999:
            fecha = datetime.date(self.ano, self.mes, 13) #
            return fecha.weekday() == 4  # la funcion weekday es un arreglo de los dias de la semana, donde el dia 4 es viernes
        else:
            return False  

# Llamar a la función principal
if __name__ == "__main__":
    metodo_main()
