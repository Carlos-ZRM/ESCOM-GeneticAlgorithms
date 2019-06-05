import math
class pi:
  def __init__(self):
    self.fact = [1,1]
    self.f = 1
    self.pi = []
    self.kas = []
  def getPi(self):
    return ''.join(self.pi)
  def factorial(self, k):
    if (k < len(self.fact)):
      return self.fact[k]
    else : 
      aux = 0
      for i in range (len(self.fact)-1, k) :
        aux = self.fact[i]*(i+1)
        self.fact.append(aux)
      return self.fact[k]
  def pik (self, k):
    res = 0.0
    pot = 6*k + 3
    f6k = self.factorial(6*k)
    f3k = self.factorial(3*k)
    fk = self.factorial(k) ** 3
    ter = 640320**pot
    ter = math.sqrt(ter)
    res = (-1**k)*f6k*(13591409+545140134*k)
    res = res / (f3k * fk * ter)
    return res
  def calculaPi(self, k):
    res = 0.0
    if k == 0 :
      res = 12 * self.pik(k)
      return 1/res
