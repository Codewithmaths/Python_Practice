""" prefect number is a number that is equal to the sum of its positive divisors excluding itself.For example, 6 is a perfect number because its positive divisors excluding itself are 1, 2, and 3, and their sum is 6. '6,28,496,8128,33550336,8589869056,137438691328 '  """

def perfect_number(n):
   if n < 1:return False 
   sum = 1
   for i in range(2, int(n**0.5) + 1):
      if n % i == 0:
         sum += i
         if i * i != n: 
            sum += n // i 
   return sum == n

print(perfect_number(137438691328)) # True


def perfect_number(n):
   sum = 0
   for i in range(1,n):
      if n % i == 0:
         sum += 1
   return sum == n
if __name__ == "__main__":
   n = int(input("Enter a number: "))
   print(perfect_number(n)) # True or False)
         