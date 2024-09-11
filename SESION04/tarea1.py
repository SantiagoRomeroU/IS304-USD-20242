import datetime

def metodo_main():
    ano = int(input("Ingrese el año : "))
    mes = int(input("Ingrese el mes : "))

    comprobador = Viernes13(ano, mes)

    if comprobador.es_viernes_13():
        print(f"Sí hay un viernes 13 en {mes}/{ano}!")
    else:
        print(f"No hay un viernes 13 en {mes}/{ano}.")


class Viernes13:
    # Constructor de la clase
    def __init__(self, ano, mes):
        self.ano = ano
        self.mes = mes

    # se valida si el dia 13 cae viernes
    def es_viernes_13(self):
        if 1 <= self.mes <= 12 and 1 <= self.ano <= 9999:
            fecha = datetime.date(self.ano, self.mes, 13)
            return fecha.weekday() == 4  # la funcion weekday es un arreglo de los dias de la semana, donde el dia 4 es viernes
        else:
            return False  

# Llamar a la función principal
if __name__ == "__main__":
    metodo_main()
