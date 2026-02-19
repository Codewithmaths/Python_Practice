""" find the gcd or hcf of two numbers"""

def gcd(a,b):
   result = min(a,b)
   while result > 0:
      if a % result == 0 and b % result == 0:
         break
      result -= 1
   return result
if __name__ == "__main__":
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))
   print(gcd(a,b))


def gcd(a,b):
   if b == 0:
      return a
   if a == 0:
      return b
   if a == b:
      return a
   if a > b:
      if a % b == 0:
         return b
      return gcd(a-b,b)
   if b > a:
      if b % a == 0:
         return a
      return gcd(a,b-a)
if __name__ == "__main__":
   a = int(input("Enter first number: "))
   b = int(input("Enter second number: "))   
   print(gcd(a,b))