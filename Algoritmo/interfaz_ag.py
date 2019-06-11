from Generadora import *
import numpy as np 
from FuncionesAG import *
class interfaz_ag:
    def __init__(self,num_elementos, num_eventos, num_padres = 2, representacion='int' ,alg_eval= eval_xx, alg_sel= sel_ruleta, alg_cruza=cruza_un_punto, alg_mutacion = mutacion_prob):
        self.alg_eval = alg_eval
        self.alg_sel = alg_sel
        self.num_eventos = num_eventos
        self.representacion = representacion
        self.espacio =  Generadora(num_elementos, representacion)
        self.num_padres = num_padres
        self.num_elementos = num_elementos
        if representacion is 'int':
            self.espacio_rep = self.espacio.getInt()
        elif representacion is 'float':
            self.espacio_rep = self.espacio.getFloat
        

        #print("Ruleta",self.alg_sel(self.espacio_rep, self.alg_eval))
    def algoritm(self):
        if self.num_elementos % 2 == 0:
            self.num_eventos = self.num_elementos // 2
        else :
            self.num_eventos = (self.num_elementos // 2)+1
        aptitud, esp_acumulada = self.alg_eval(self.espacio_rep)
        
        r = self.alg_sel(self.num_eventos, aptitud, esp_acumulada)
        print("r",r)
        #for i in range(num_eventos):
            

iag = interfaz_ag(4,5)
iag.algoritm()
l = [0,2,3,4,5]
print('l',l[])
'''
a = BitArray_gr(int = 31,length=32)
b = BitArray_gr(int = 13,length=32)
cruza_un_punto(a,b,5)
print(a.bin)
c = mutacion_prob(a,5)
print(c.bin)


sub = a.bin[32-5:]
aux = [ j if np.random.random() >= .2 else str(int(not int(j))) for j in sub  ]
print("sub",'0b'+(''.join(aux)) )
print(np.random.random_sample())
'''