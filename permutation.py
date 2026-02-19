""" find the permutation solution  """
def calculate_npr(n, r):
    if r > n:
        return 0
    result = 1
    for i in range(r):
        result *= (n - i)
        
    return result
if __name__ == "__main__":
    n = int(input("Enter the value of n: "))
    r = int(input("Enter the value of r: "))
    print(calculate_npr(n, r))


class Factorial:
   def fact(self,n):
      if n == 0 or n == 1:
         return 1
      else:
         return n * self.fact(n-1)
if __name__ == "__main__":
   n = int(input("Enter the value of n: "))
   print(Factorial().fact(n))

class Permutation(Factorial):
   def calculate_npr(self,n,r):
      if r > n:
         return 0
      return self.fact(n) // self.fact(n-r)
if __name__ == "__main__":
   n = int(input("Enter the value of n: "))
   r = int(input("Enter the value of r: "))
   print(Permutation().calculate_npr(n, r))