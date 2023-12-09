import math
class complessi:
  def __init__(self, a=0, b=0):
    self.a = a
    self.b = b

  def Somma(self,Z1):
    Z=complessi()
    Z.a=self.a+Z1.a
    Z.b=self.b+Z1.b
    return Z
  #idem per la Sottrazione
  def Prodotto(self,Z1):
    Z=complessi()
    Z.a=self.a*Z1.a-self.b*Z1.b
    Z.b=self.a*Z1.b - self.b*Z1.a
    return Z
  def coniugato(self,Z1):
    Z=complessi()
    Z.a=Z1.a
    Z.b=-Z1.b
    return Z

  def modulo(self):
    m=math.sqrt(math.pow(self.a,2)+math.pow(self.b,2))
    return m

  def StampaComplesso(self):
    if self.b>=0:
      print(f"z={self.a}+{self.b}i")
    else:
      print(f"z={self.a}-{abs(self.b)}i")
