""" check that a string is a palindrome or not """


""" first method: reverse the string and compare it with the original string
   time complexity: O(n)
   space complexity: O(n)
"""
from xmlrpc.client import FastMarshaller


def is_palindrome(s):
   s = s.lower().replace(" ", "")
   return s == s[::-1]
if __name__ == "__main__":
   s = input("Enter a string: ")
   print(is_palindrome(s))


""" second method: use two pointers to compare characters from the start and end of the string
   time complexity: O(n)
   space complexity: O(1)
"""
def string_palindrone(s):
   left , right = 0 , len(s) - 1
   while left < right:
      if s[left] != s[right]:
         return False
      left += 1
      right -= 1
   return True
if __name__ == "__main__":
   s = input("Enter a string: ")
   print(string_palindrone(s))


"""chech the integer is a palindrome or not
   time complexity: O(n)
   space complexity: O(1)
"""
def is_palindrome_number(num):
   if num <0:
      return False
   original_num = num
   reversed_num = 0
   while num >0:
      digit = num % 10
      reversed_num = (reversed_num * 10) + digit
      num //= 10
   return original_num == reversed_num
if __name__ == "__main__":
   num = int(input("Enter an integer: "))
   print(is_palindrome_number(num))