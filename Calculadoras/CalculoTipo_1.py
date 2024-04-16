from DatosEntrada import DatosEntrada
from Calculadora_T1 import Calculadora_T1
from Calculadora_T2 import Calculadora_T2

def main():

    t_busqueda = int(input("Introduzca tiempo de buscqueda: "))
    v_rotacional = int(input("Introduzca velocidad rotacional: "))
    sectores_pista = int(input("Introduzca numero de sectores/pista: "))
    bytes_sector = int(input("Introduzca bytes/sector: "))
    bytes_peticion = int(input("Introduzca bytes de la peticion: "))
    datos1 = DatosEntrada(t_busqueda,v_rotacional,sectores_pista,bytes_sector,bytes_peticion)
    print(datos1)
    calculo1 = Calculadora_T1(t_busqueda,v_rotacional,sectores_pista,bytes_sector,bytes_peticion)
    print(calculo1)
    calculo2 = Calculadora_T2(t_busqueda,v_rotacional,sectores_pista,bytes_sector,bytes_peticion)
    print(calculo2)


if __name__ == "__main__":
    main()