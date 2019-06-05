from Generadora import *

class Algoritmo_Genetico:
    def __init__(self,num_elementos, representacion, alg_eval , alg_sel):
        self.alg_eval = alg_eval
        self.alg_sel = alg_sel
        self.representacion = representacion
        self.espacio =  Generadora(num_elementos, representacion)

    def eval_xx(self,elementos):
        return list(map(lambda x: x**2),elementos)
    def sel_ruleta(self):
        apitud = []
        esperanza = []
        sum_total = 0.

        aptitud = self.eval_xx()
        sum_total = reduce(lambda a,b : a+b,aptitud)
        esperanza = list (map(apitud))

    li = []    
    li = list(range(10))
    print(li)
    ac=[sum(li[0:x+1]) for x in range(0,len(li))]
    print(ac)