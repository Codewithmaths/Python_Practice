""" First method to generate Fibonacci series using recursion with memoization. """
memo = {0: 0, 1: 1}
def fibo(n):
   if n in memo:
      return memo[n]
   
   memo[n] = fibo(n-1) + fibo(n-2)
   return memo[n]
print(fibo(100))  # Output: 55

""" Second method to generate Fibonacci series. """
def nFibo(n):
   if n <= 0: return 0
   if n == 1: return 1
   a, b = 0, 1
   for i in range(2, n + 1):
      a, b = b, a + b
   return b
print(nFibo(100))  # Output: 55

""" Third method to generate Fibonacci series using formular. """

import math
def fibo(n):
   phi = (1 + math.sqrt(5)) / 2
   return round((phi ** n) / math.sqrt(5))
print(fibo(100))