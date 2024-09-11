/*
 * Crea una función que sea capaz de detectar si existe un viernes 13 en el mes y el año indicados.
 * - La función recibirá el mes y el año y retornará verdadero o falso.
 */ 
import datetime

def MetodoMain():
    anio = int(input("Ingrese el año (1-9999): "))
    mes = int(input("Ingrese el mes (1-12): "))
    
class Viernes13:
    /*constructor*/
    def __init__(self, anio, mes):
        self.anio = anio
        self.mes = mes
