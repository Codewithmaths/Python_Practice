""" Happy Number is a number which eventually reaches 1 when replaced repeatedly by the sum of the square of its digits. If it loops endlessly in a cycle which does not include 1, then it is not a happy number."""
def isHappy(n: int) -> bool:
   seen = set()
   while n != 1 or n not in seen:
      seen.add(n)
      total = 0
      while n > 0:
         digit = n % 10
         total += digit**2
         n //= 10
      n = total
   return n == 1

if __name__ == "__main__":
   # n = int(input("Enter a number: "))
   print(isHappy(40))