from Generadora import *
import numpy as np 
from FuncionesAG import *
class interfaz_ag:
    def __init__(self,num_elementos, representacion='int', alg_eval= eval_xx, alg_sel= sel_ruleta):
        self.alg_eval = alg_eval
        self.alg_sel = alg_sel
        self.representacion = representacion
        self.espacio =  Generadora(num_elementos, representacion)
        if representacion is 'int':
            self.espacio_rep = self.espacio.getInt()
        print("Ruleta",self.alg_sel(self.espacio_rep, self.alg_eval))

iag = interfaz_ag(4)
