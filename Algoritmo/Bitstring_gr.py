from bitstring import BitArray 
class BitArray_gr(BitArray):
   #def __init__(self, val = 0, ln=16):
   #   self.bit_str = BitArray(int=val, ln=16)
   def __init__(self, auto=None, length=16, offset=None, **kwargs):
   #def __init__(self , val):
      BitArray.__init__(self,auto,length, offset,  **kwargs)
      self.d_gray = ""
      self._setgray()
      #super.__init__(self, int=val, length=8 )
   def _getgray(self):
      return self.d_gray
   def _setgray(self):
      #r = BitArray(int=val, length=8)
      
      #r2 = r >> 1
      #r2 ^=r
      r =self.__copy__()>>1
      r ^= self
      self.d_gray = r.bin
   
   gray = property(_getgray,_setgray)
#l = list(range(10))
'''
for i in range(16):
   b = BitArray_gr(int = i, length=16)
   print(b.gray)
   
m = list(map(BitArray_gr, l))
print(m)
'
for i in l:
   j = binario_gray(i)
   print(j.bin)
'''