from Generadora import *
import numpy as np 
from functools import reduce, partial
def eval_xx(elementos):
    aptitud = []
    esperanza = []
    sum_total = 0.
    
    elementos=sorted(elementos)
    
    print("espacio", elementos)
    aptitud = list(map(lambda x: x**2,elementos))
    print("array aptitud",aptitud)
    sum_total = reduce(lambda a,b : a+b,aptitud)
    print("Suma fi", sum_total)
    
    esperanza = list (map(lambda x :x/sum_total, aptitud ))
    print("Esperanza", esperanza)
    esp_acumulada = [sum(esperanza[0:x+1]) for x in range(0,len(esperanza))]
    print("Esperanza Acumulada", esp_acumulada)
    return elementos, esp_acumulada

def sel_ruleta(num_eventos, aptitud, esp_acumulada ):
    r = set()
    c = 0
    print("\n\n********\n",esp_acumulada)
    while len(r) < num_eventos:
            # Generar un numero T [0,1)
        prob = np.random.random_sample()
        print("tao",prob)
        #r = list(filter(lambda x: x  > prob, esp_acumulada ))
        aux = [ aptitud[i] for i in range (len(aptitud)) if esp_acumulada[i] >= prob]
        
        saux = set(aux)
        r.update(saux)
        print(r)
        c+=1
        if(c> num_eventos**2):
           print("Tao muy grande")
           print(prob,esp_acumulada,r)
           r.update(set(aptitud))
           break
    r=sorted(list(r))
    print("Padres seleccionados",r[len(r)-num_eventos:])
        
    '''
    for i in range(len(esp_acumulada)):
        if prob <= esp_acumulada[i] and prob >esp_acumulada[i-1] :
            elemento = i
            break
    return elemento 
    '''
    return list(r)[len(r)-num_eventos:]
def cruza(alg_cruza, padres, longitud=5):
    aux = []
    if (len(padres)%2==0):
        for i in list(range(0,len(padres),2)):
            aux +=  alg_cruza(padres[i],padres[i+1],longitud)     
 
    else :
        aux = [padres[i] for i in list(range(0,len(padres)-1,2)) ]
    #ret = [f]
    
    return padres+aux
def cruza_un_punto (x1,x2, longitud):
    r = np.random.randint(1, longitud  )
    #r = BitArray_gr(int = rand,length=32)
    r = 4
    #r1 = BitArray_gr(int = rand,length=32)
    #r2 = BitArray_gr(int = (longitud - rand) ,length=32)
    #print("r",r1.int, r2.int)
    
    a = BitArray_gr(int = x1, length=32)
    b = BitArray_gr(int = x2, length=32)
    aux = BitArray_gr(int = (2**longitud)-1,length=32)
    h1 = BitArray_gr(int = 0,length=32)
    h2 = BitArray_gr(int = 0,length=32)
    
    #aux = (2**longitud)-1
    #print(aux.int)

    aux1 = aux << r
    aux2 = aux >> longitud - r
    a0 = a & aux1
    a1 = a & aux2
    b0 = b & aux1
    b1 = b & aux2
    h1 = a0 | b1
    h2 = b0 | a1
    
    print(a.bin,b.bin)
    print(a0.bin , a1.bin)
    print(b0.bin , b1.bin)
    print(h1.bin)
    print(h2.bin)
    '''
    print("\n\n Mutacion en un punto", r)
    print("{0:b}".format(a))
    print("{0:b}".format(b))
    print("{0:b}".format(h1))
    print("{0:b}".format(h2))
    '''
    return int(h1.int), int(h2.int)
    #return x1,x2
def mutacion_prob(a, longitud=5):
    a = BitArray(int = a, length=32)
    sub = a.bin[32-longitud:]
    prob = 1/(2*longitud)
    aux = [ j if np.random.random_sample() >= prob else str(int(not int(j))) for j in sub  ]
    rs = '0'*(32-longitud)
    rs = '0b'+rs+(''.join(aux))
    return BitArray(rs).int 
    
