# Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
# La función recibirá el mes y el año y retornará verdadero o falso.
 
import datetime

def MetodoMain():
    ano = int(input("Ingrese el año (1-9999): "))
    mes = int(input("Ingrese el mes (1-12): "))

    comprobador = Viernes13(ano, mes)

    if comprobador.es_viernes_13():
        print(f"Sí hay un viernes 13 en {mes}/{ano}!")
    else:
        print(f"No hay un viernes 13 en {mes}/{ano}.")

class Viernes13:
    #constructor de la clase
    def __init__(self, ano, mes):
        self.ano = ano
        self.mes = mes

    def es_viernes_13(self):
        if mes >= 1 and mes <= 12 and ano >= 1 and ano <= 9999:
            fecha = datetime.date(self.ano, self.mes, 13)
            return fecha.weekday() == 4
        else:
            return false

