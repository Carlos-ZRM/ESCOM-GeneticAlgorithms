import numpy as np
import copy
def quick(lista, inferior , superior):
  if (inferior > superior or inferior == superior):
    return 0
  pivote = lista[superior]
  i = inferior 
  j = superior - 1
  aux = 0
  c = 0
  while ( j > i):
    #print (i, j, pivote) 
    if ( lista[j] < pivote and lista[i] >= pivote ):
      aux = lista[j]
      lista[j] = lista[i]
      lista[i] = aux
      i += 1
      j -= 1
      c+=1
    if lista[i] < pivote:
      i+=1
      c+=1
    if lista[j] >= pivote:
      j-=1
      c+=1
  if (lista[i] > pivote ):
    lista[superior] = lista[i]
    lista[i] = pivote
    c+=1
  else:
    i+=1
  c+= quick(lista, inferior , i-1)
  c+= quick(lista, j+1 , superior)
  return c

def burbuja (lista):
  l = len(lista)
  aux = 0
  c = 0
  for i in range (l):
    for j in range (0, l-i-1):
      if lista[j]> lista[j+1]:
        aux = lista[j]
        lista[j] = lista[j+1]
        lista[j+1] = aux
      c+=1
  return (c)
c = 0
l = [5 , 3 , 7 , 6 , 2 ,5, 1 ,4]
#l = np.random.randint(1, 100, 20 ) 
#l = [990, 862, 741 ,872, 387, 139,862 ,449 ,450, 778 ,562] 
#l = [572, 225, 881, 292, 274, 496 ,725 ,977, 508, 178 ,399, 717,881 ,299, 841 ,191,881]
l = np.random.randint(1, 1000, 500 )
#l = list(range(0,500))
#l = list(range (500,0, -1))
print (l)
b = copy.copy(l)
c = quick(l, 0 , len(l)-1 )
c2 = burbuja(b)
print ( "\n\n\n Quick",c, len(l))
print ( "\n\n\n Burbuja",c2, len(l))
