from Generadora import *
import numpy as np 
from FuncionesAG import *
import matplotlib.pyplot as plt

class interfaz_ag:
    def __init__(self,num_elementos, num_eventos, num_padres = 2, representacion='int' ,alg_eval= eval_xx, alg_sel= sel_ruleta, alg_cruza=cruza_un_punto, alg_mutacion = mutacion_prob):
        self.alg_eval = alg_eval
        self.alg_sel = alg_sel
        self.num_eventos = num_eventos
        self.representacion = representacion
        self.espacio =  Generadora(num_elementos, representacion)
        self.num_padres = num_padres
        self.num_elementos = num_elementos
        #self.espacio_rep =[]

        if representacion is 'int':
            self.espacio_rep = self.espacio.getInt()
        elif representacion is 'float':
            self.espacio_rep = self.espacio.getFloat
        #self.espacio_rep = self.espacio

        #print("Ruleta",self.alg_sel(self.espacio_rep, self.alg_eval))
    def algoritm(self):
        maximos =[]
        minimos =[]
        if self.num_elementos % 2 == 0:
            self.num_padres = self.num_elementos // 2
        else :
            self.num_padres = (self.num_elementos // 2)+1
        '''
        ******
            Evaluate P_k
        ******
        '''
        aptitud, esp_acumulada = self.alg_eval(self.espacio_rep)
        #print("eventos",  self.num_eventos )
        
        ma = max(aptitud)
        mi = min(aptitud)
        maximos.append(ma)
        minimos.append(mi)
        
        '''
        ******
            WHile
        ******
        '''
        for i in range(self.num_eventos):
            padres = self.alg_sel(self.num_padres, aptitud, esp_acumulada)
            '''
            ******
            Crossover
            ******
            '''
            padres = cruza(cruza_un_punto, padres)
            print(padres)
            '''
            ******
            Mutate
            ******
            '''
            padres = list(map(mutacion_prob,padres))
            print(padres)
            aptitud, esp_acumulada = self.alg_eval(padres )
            ma = max(aptitud)
            mi = min(aptitud)
            maximos.append(ma)
            minimos.append(mi)
        
        y = list(range(len(maximos)))
        fig, ax = plt.subplots()
        print("listas",self.num_eventos)
        print(y,maximos)
        print(y, minimos)
        ax.plot( maximos)
        ax.plot(  minimos)
   
        #ax.plot( minimos )
        ax.grid()
        fig.show()
        fig.savefig("xoxo.png")
        #print("r",padres)
        #for i in range(num_eventos):
            

iag = interfaz_ag(8,100)
iag.algoritm()

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