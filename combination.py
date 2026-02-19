""" solve the combination problem """

class Factorial:
   def fact(self,n):
      if n == 0 or n == 1:
         return 1
      else:
         return n * self.fact(n-1)
if __name__ == "__main__":
   n = int(input("Enter the value of n: "))
   print(Factorial().fact(n))

class Combination(Factorial):
   def combination(self,n,r):
      return self.fact(n) // (self.fact(r) * self.fact(n-r))
if __name__ == "__main__":
   n = int(input("Enter the value of n: "))
   r = int(input("Enter the value of r: "))  
   print(Combination().combination(n,r))



def calculate_ncr(n, r):
    if r > n: return 0
    if r == 0 or r == n: return 1

    if r > n // 2:
        r = n - r
        
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= (n - i)
        denominator *= (i + 1)
        
    return numerator // denominator
if __name__ == "__main__":
   n = int(input("Enter the value of n: "))
   r = int(input("Enter the value of r: "))  
   print(calculate_ncr(n,r))