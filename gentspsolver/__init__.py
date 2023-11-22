def my_sum(x, y):
    """A function that sums. """
    return x+y


def my_mul(x, y):
    """A function that multiply. """
    return x*y

import math

#Calcula el máximo común divisor utilizando el algorítmo de Euclides
def gcd(a,b):
  while b:
    a,b = b, a%b
  return a

#Genera las ternas pitagóricas primitivas hasta un z<k con k un número entero positivo
def genera_tp(k):
  ternas_pitagoricas = [] #Inicia una lista vacía para almacenar las ternas pitagóricas primitivas
  for m in range(2, int(math.sqrt(k))):
    for n in range(1,m):
      if gcd(m,n) == 1: #Verifica si m y n son primos relativos (condición de primitividad)
        x = m**2-n**2
        y = 2*m*n
        z = m**2+n**2
        if z < k:
          ternas_pitagoricas.append((x,y,z))
  return ternas_pitagoricas
