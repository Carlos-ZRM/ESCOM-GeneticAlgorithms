from Generadora import *
import numpy as np 
class interfaz_ag:
    def __init__(self,num_elementos, representacion='int', alg_eval= sel_ruleta, alg_sel=self.sel_ruleta):
        self.alg_eval = alg_eval
        self.alg_sel = alg_sel
        self.representacion = representacion
        self.espacio =  Generadora(num_elementos, representacion)
        if representacion is 'int':
            self.espacio_rep = self.espacio.getInt()
        alg_sel()
    def eval_xx(self,elementos):
        return list(map(lambda x: x**2),elementos)
    def sel_ruleta(self):
        apitud = []
        esperanza = []
        sum_total = 0.

        aptitud = self.eval_xx(self.espacio_rep)
        sum_total = reduce(lambda a,b : a+b,aptitud)
        esperanza = list (map(apitud))
        esp_acumulada = [sum(li[0:x+1]) for x in range(0,len(li))]
        prob = np.random.random_sample()
        elemento = 0
        for i in range(len(esp_acumulada)):
            if prob <= esp_acumulada[i] & prob >esp_acumulada[i-1] :
                elemento = i
                break
        return elemento 
  