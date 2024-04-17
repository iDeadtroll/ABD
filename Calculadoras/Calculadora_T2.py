from DatosEntrada import DatosEntrada

class Calculadora_T2(DatosEntrada):

    def T_transferencia_sector(self):
        return round((1/self.v_rotacional),3)/self.sectores_pista
    
    def N_sectores_peticion(self):
        return self.bytes_peticion / self.bytes_sector
    
    def N_sectores_leidos(self):
        return self.N_sectores_peticion() + self.sectores_X
    
    def T_Tranferencia(self):
        return round(self.T_transferencia_sector(),4) * self.N_sectores_leidos()
    
    def __str__(self):
        datos = "\n\nCalculo 2: "

        datos += "\nTiempo de trasferencia por sector = tiempo de latencia rotacional / sectores/pista"
        datos += "\nTiempo de trasferencia por sector = " + str(round((1/self.v_rotacional),3)) + " / " + str(self.sectores_pista)
        datos += "\nTiempo de trasferencia por sector = " + str(round(self.T_transferencia_sector(),4))
        datos += "\nNumero de sectores de la peticion = bytes de la peticion / bytes/sector"
        datos += "\nNumero de sectores de la peticion = " + str(self.bytes_peticion) + " / " + str(self.bytes_sector)      
        datos += "\nNumero de sectores de la peticion = " + str(round(self.N_sectores_peticion(),4))
        datos += "\nNumero de sectores X = " + str(round(self.sectores_X,4))
        datos += "\nNumero de sectores leidos = sectores de la peticion + sectores X"
        datos += "\nNumero de sectores leidos = " + str(round(self.N_sectores_peticion(),4)) + " + " + str(round(self.sectores_X,4))
        datos += "\nNumero de sectores leidos = " + str(round(self.N_sectores_leidos(),4))
        datos += "\nTiempo de transferencia = tiempo de tranferencia/sector * numero de sectores leidos"
        datos += "\nTiempo de transferencia = " + str(round(self.T_transferencia_sector(),4)) + " * " + str(round(self.N_sectores_leidos(),4))
        datos += "\nTIEMPO DE TRANSFERENCIA = " + str(round(self.T_Tranferencia(),4))
        
        return datos