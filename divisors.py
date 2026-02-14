import math
class Divisors:
   def allDivisors(self,n:int):
      divisors = []
      for i in range (1,int(math.sqrt(n)+1)):
         if n % i == 0:
            if n/i == i:
               print(i,end=" ")
            else:
               print(i,end=" ")
               # print(int(n/i),end=" ")
               divisors.append(int(n/i))
      for i in divisors[::-1]:
         print(i,end=" ")

print(Divisors().allDivisors(100))
