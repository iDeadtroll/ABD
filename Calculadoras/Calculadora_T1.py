from DatosEntrada import DatosEntrada

class Calculadora_T1(DatosEntrada):

    @property
    def t_latencia_rot(self):
        return 1/self.v_rotacional
    
    def t_medio_latencia_rot(self):
        return 1/(2*self.v_rotacional)

    def t_acceso(self):
        return round((self.t_busqueda + self.t_medio_latencia_rot()),4)
    
    def __str__(self):
        # datos = super().__str__() + "\n"
        datos = "\n\nCalculo 1: "
        datos += "\nTiempo de latencia rotacional: " + str(round(self.t_latencia_rot,4)) + " seg"
        datos += "\nTiempo medio de latencia rotacional: " + str(round(self.t_medio_latencia_rot(),4)) + " seg"
        datos += "\nTiempo de acceso  =  tiempo de busqueda + Tiempo medio de latencia rotacional"
        datos += "\nTiempo de acceso  = " + str(self.t_busqueda) + " + " + str(round(self.t_medio_latencia_rot(),4))
        datos += "\nTIEMPO DE ACCESO  = " + str(self.t_acceso()) + " seg"
        datos += "\n"
        return datos

