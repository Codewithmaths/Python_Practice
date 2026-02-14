# first method
import math
def addfractions(a,b):
   res_num = a[0]*b[1] + a[1]*b[0]
   res_den = a[1]*b[1]
   gcd = math.gcd(res_num,res_den)
   return (res_num//gcd,res_den//gcd)

print(addfractions((1,2),(3,2)))


# second method

from fractions import Fraction

f1 = Fraction(1, 2)
f2 = Fraction(3, 2)

result = f1 + f2
print(result)

# third method
from math import gcd
def add_Fractions(a, b):
   den = gcd(a[1], b[1])
   den = (a[1] * b[1]) // den
   num = (a[0] * (den // a[1])) + (b[0] * (den // b[1]))
   common = gcd(num, den)
   return (num // common, den // common)

if __name__ == "__main__":
   a = (1, 2)
   b = (3, 2)
   ans = add_Fractions(a, b)
   print(ans)
   print(f"{ans[0]},{ans[1]}")
