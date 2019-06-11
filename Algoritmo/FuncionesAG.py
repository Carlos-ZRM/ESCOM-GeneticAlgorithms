from Generadora import *
import numpy as np 
from functools import reduce, partial
def eval_xx(elementos):
    aptitud = []
    esperanza = []
    sum_total = 0.
    elementos=sorted(elementos)
    print("espacio", elementos)
    #aptitud = al_eval(espacio_rep)
    aptitud = list(map(lambda x: x**2,elementos))
    print("array aptitud",aptitud)
    sum_total = reduce(lambda a,b : a+b,aptitud)
    print("Suma fi", sum_total)
    
    esperanza = list (map(lambda x :x/sum_total, aptitud ))
    print("Esperanza", esperanza)
    esp_acumulada = [sum(esperanza[0:x+1]) for x in range(0,len(esperanza))]
    print("Esperanza Acumulada", esp_acumulada)
    return elementos, esp_acumulada
    #return list(map(lambda x: x**2,elementos))

def sel_ruleta(num_eventos, aptitud, esp_acumulada ):
    r = set()
    while len(r) < num_eventos:
        prob = np.random.random_sample()
        print("tao",prob)
        elemento = 0
        #r = list(filter(lambda x: x  > prob, esp_acumulada ))
        aux = [ aptitud[i] for i in range (len(aptitud)) if esp_acumulada[i] >= prob]
        print(aux)
        saux = set(aux)
        r.update(saux)
        print(r)
        
    '''
    for i in range(len(esp_acumulada)):
        if prob <= esp_acumulada[i] and prob >esp_acumulada[i-1] :
            elemento = i
            break
    return elemento 
    '''
    return r
def cruza_un_punto (a,b, longitud):
    r = np.random.randint(1, longitud  )
    #r = BitArray_gr(int = rand,length=32)
    r = 3
    #r1 = BitArray_gr(int = rand,length=32)
    #r2 = BitArray_gr(int = (longitud - rand) ,length=32)
    #print("r",r1.int, r2.int)
    aux = BitArray_gr(int = (2**longitud)-1,length=32)
    h1 = BitArray_gr(int = 0,length=32)
    h2 = BitArray_gr(int = 0,length=32)
    
    #print(aux.int)

    aux1 = aux << r
    aux2 = aux >> longitud - r
    a0 = a & aux1
    a1 = a & aux2
    b0 = b & aux1
    b1 = b & aux2
    h1 = a0 | b1
    h2 = b0 | a1
    '''
    print(a.bin,b.bin)
    print(a0.bin , a1.bin)
    print(b0.bin , b1.bin)
    print(h1.bin)
    print(h2.bin)
    '''
    return h1,h2
    
def mutacion_prob(a, longitud):
    sub = a.bin[32-longitud:]
    prob = 1/longitud
    aux = [ j if np.random.random_sample() >= prob else str(int(not int(j))) for j in sub  ]
    rs = '0'*(32-longitud)
    rs = '0b'+rs+(''.join(aux))
    return BitArray(rs) 
    
