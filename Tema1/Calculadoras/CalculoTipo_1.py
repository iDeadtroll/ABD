from DatosEntrada import DatosEntrada
from Calculadora_T1 import Calculadora_T1
from Calculadora_T2 import Calculadora_T2


def main():



    t_busqueda = int(input("Introduzca tiempo de busqueda: "))
    v_rotacional = int(input("Introduzca velocidad rotacional: "))
    sectores_pista = int(input("Introduzca numero de sectores/pista: "))
    bytes_sector = int(input("Introduzca bytes/sector: "))
    bytes_peticion = float(input("Introduzca KiB de la peticion: "))
    sectores_X = int(input("Introduzca numero de sectores X: "))
    datos1 = DatosEntrada(t_busqueda,v_rotacional,sectores_pista,bytes_sector,bytes_peticion,sectores_X)
    print(datos1)
    calculo1 = Calculadora_T1(t_busqueda,v_rotacional,sectores_pista,bytes_sector,bytes_peticion,sectores_X)
    print(calculo1)
    calculo2 = Calculadora_T2(t_busqueda,v_rotacional,sectores_pista,bytes_sector,bytes_peticion,sectores_X)
    print(calculo2)

    print("\nTiempo de peticion =  Tiempo de acceso + Tiempo de tranferencia")
    print("\nTIEMPO DE PETICION = " + str(calculo1.t_acceso()) + " + " + str(calculo2.T_Tranferencia()) )
    print("\nTIEMPO DE PETICION = " + str(round((calculo1.t_acceso()*2 + calculo2.T_Tranferencia()),4)))
    print("\nVelocidad de tranferencia maxima = " + str(round((datos1.v_rotacional*datos1.sectores_pista*datos1.bytes_sector)/1024,4)))


if __name__ == "__main__":
    main()