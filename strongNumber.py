""" Strong Number is the number that the sum of the factorial of its digits is equal to the original number."""

class Factorial: # Define a class named Factorial

   def __init__(self): # Constructor method
       pass
    
   def get_factorial(self,num): # Method to calculate factorial
    if num == 0 or num == 1:
        return 1
    else:
        return num * self.get_factorial(num - 1)
    
fact = Factorial() # Create an instance of the Factorial class

print(fact.get_factorial(5)) # 120


class StrongNumber(Factorial):
    def is_strong_number(self,number):
        temp = number
        total_sum = 0
        while temp > 0:
            digit = temp % 10
            total_sum += self.get_factorial(digit)
            temp //= 10
        return total_sum == number 

SN = StrongNumber() # Create an instance of the StrongNumber class

print(SN.get_factorial(10)) # 3628800
print(SN.is_strong_number(145)) # True)