from juegobn import juegobn
from utilerias import utilerias

class Examen(juegobn):
    def __init__(self):
        super().__init__()
        self.utils = utilerias()
        self.carga_matriz_file()
        self.matriz[3][0] = "E"
        self.matriz[3][1] = "X"
        self.matriz[3][2] = "A"
        self.matriz[3][3] = "M"
        self.matriz[3][4] = "E"
        self.matriz[3][5] = "N"
        self.matriz[4][0] = "F"
        self.matriz[4][1] = "I"
        self.matriz[4][2] = "N"
        self.matriz[4][3] = "A"
        self.matriz[4][4] = "L"


obj_exa = Examen()
obj_exa.muestra_matriz()
obj_exa.descarga_matriz()