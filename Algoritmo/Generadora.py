import numpy as np
from Bitstring_gr import * 
class Generadora:
    def __init__(self,num_elementos,d_types, max=1000) :
        shape, scale = 2., 2.  # mean=4, std=2*sqrt(2)
        numeros = np.random.gamma(shape, scale, num_elementos)
        #numeros = list(range(10))
        print(len(numeros))
        self.espacio = []
        if d_types is 'float' :
            print("0")
            self.espacio = list(map(lambda x: BitArray_gr(float = x,length=32),numeros))
        elif d_types is 'int':
            numeros = list(map(lambda x : int( (x * max)/10 ),numeros) )
            self.espacio = list(map(lambda x: BitArray_gr(int = x,length=32),numeros))
    def getInt(self):
        return list(map( lambda x : x.int,  self.espacio)) 
    def getBin(self):
        return list(map( lambda x : x.bin,  self.espacio)) 
    def getFloat(self):
        return list(map( lambda x : x.float,  self.espacio)) 
    def getGray(self):
        return list(map( lambda x : x.gray,  self.espacio)) 
       
        #for i in self.espacio:
        #    print(i.int)
        #print(self.espacio)
#G = Generadora(100, 'int')