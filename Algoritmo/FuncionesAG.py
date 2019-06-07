from Generadora import *
import numpy as np 
from functools import reduce, partial
def eval_xx(elementos):
    return list(map(lambda x: x**2,elementos))

def sel_ruleta(espacio_rep, al_eval=eval_xx ):
    apitud = []
    esperanza = []
    sum_total = 0.
    print("espacio", espacio_rep)
    aptitud = al_eval(espacio_rep)
    print("array aptitud",aptitud)
    sum_total = reduce(lambda a,b : a+b,aptitud)
    print("Suma fi", sum_total)
    
    esperanza = list (map(lambda x :x/sum_total, aptitud ))
    print("Esperanza", esperanza)
    esp_acumulada = [sum(esperanza[0:x+1]) for x in range(0,len(esperanza))]
    print("Esperanza Acumulada", esp_acumulada)
    prob = np.random.random_sample()
    elemento = 0
    for i in range(len(esp_acumulada)):
        if prob <= esp_acumulada[i] and prob >esp_acumulada[i-1] :
            elemento = i
            break
    return elemento 
  