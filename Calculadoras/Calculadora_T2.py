from DatosEntrada import DatosEntrada

class Calculadora_T2(DatosEntrada):

    def T_transferencia_sector(self):
        return (1/self.v_rotacional)/self.sectores_pista
    
    def N_sectores_peticion(self):
        return self.bytes_peticion / self.bytes_sector
    
    def N_sectores_X(self):
        return self.sectores_pista - self.N_sectores_peticion()

    def N_sectores_leidos(self):
        return self.N_sectores_peticion() + self.N_sectores_X()
    
    def T_Tranferencia(self):
        return self.T_transferencia_sector() * self.N_sectores_leidos()
    
    def __str__(self):
        datos = "\n\nCalculo 2: "
        datos += "\nTiempo de trasferencia: " + str(round(self.T_Tranferencia(),4))
        return datos