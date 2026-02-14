""" Permutation Circular Table"""


""" First method using while loop"""
def permutation_circular_table(n):
   result = 1
   while n >0:
      result *= n
      n -= 1
   return result

if __name__ == "__main__":
   n = int(input("Enter the number of people: "))
   print("Number of ways to arrange", n, "people around a circular table is:", permutation_circular_table(n-1))


""" Second method using math module"""
import math
def circular_permutations(n):
    if n <= 1:
        return 1
    # Formula: (n - 1)!
    return math.factorial(n - 1)
if __name__ == "__main__":
   n = int(input("Enter the number of people: "))
   print("Number of ways to arrange", n, "people around a circular table is:", circular_permutations(n))