""" find the lcm of two numbers """
def lcm(a, b):
   g = max(a, b)
   s = min(a, b)

   for i in range(g, a * b + 1, g):
      if i % s == 0:
         return i
   return a * b
if __name__=="__main__":
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
   print(lcm(a, b))