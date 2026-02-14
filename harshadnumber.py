""" Harshad Number is a number that is divisible by the sum of its digits."""

""" First method using while loop and modulus operator."""
def is_harshad_number(num):
   if num <= 0:
      return False
   temp = num
   digit_sum = 0
   while temp > 0:
      digit_sum += temp % 10
      temp //= 10
   return num % digit_sum == 0
if __name__ == "__main__":
   n = int(input("Enter a number: "))
   print(is_harshad_number(n)) # True or False

""" Second method using list comprehension and sum() function."""
def isHarshadNumber(num):
   if num <= 0:
      return False
   digit_sum = sum(int(digit) for digit in str(num))
   return num % digit_sum == 0
if __name__ == "__main__":
   n = int(input("Enter a number: "))
   print(isHarshadNumber(n)) # True or False


""" Nth Harshad Number using while loop."""
def find_nth_harshad(n):
    count = 0
    num = 0
    while count < n:
        num += 1
        if isHarshadNumber(num):
            count += 1
            
    return num
if __name__ == "__main__":
   n = int(input("Enter a number: "))
   print(find_nth_harshad(n)) # Nth Harshad Number
