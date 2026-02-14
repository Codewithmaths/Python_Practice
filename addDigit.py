""" First method to add digits using mathematical approach """
def addDigit(num):
   if num == 0: return 0
   return 1 + (num - 1) % 9

print(addDigit(38)) # Output: 2


""" Second method to add digits using iterative approach """
def addDigit(num):
   while num >= 10:
      num = sum(int(digit) for digit in str(num))
   return num
print(addDigit(38)) # Output: 2

""" Third method to add digits using recursive approach """
def addDigit(num):
   if num < 10:
      return num
   return addDigit(sum(int(digit) for digit in str(num)))
print(addDigit(38)) # Output: 2

""" fouth method to add digits """
def addDigit(num):
   while num >= 10:
      total = 0
      while num > 0:
         total += num % 10
         num //= 10
      num = total
   return num
print(addDigit(38)) # Output: 2


