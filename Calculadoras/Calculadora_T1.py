from DatosEntrada import DatosEntrada

class Calculadora_T1(DatosEntrada):

    @property
    def t_latencia_rot(self):
        return 1/self.v_rotacional
    
    def t_medio_latencia_rot(self):
        return 1/(2*self.v_rotacional)

    def t_acceso(self):
        return self.t_busqueda + self.t_medio_latencia_rot()
    
    def __str__(self):
        # datos = super().__str__() + "\n"
        datos = "\n\nCalculo 1: "
        datos += "\nTiempo de latencia rotacional: " + str(round(self.t_latencia_rot,4)) + " seg"
        datos += "\nTiempo medio de latencia rotacional: " + str(round(self.t_medio_latencia_rot(),4)) + " seg"
        datos += "\nTiempo de acceso: " + str(round(self.t_acceso(),4)) + " seg"
        return datos

