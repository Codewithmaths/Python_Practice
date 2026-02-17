""" reversed string """


""" first method: reverse a string using slicing """
def reverseStringSlicing(s):
   return s[::-1]
if __name__ == "__main__":
   s = input("Enter a string: ")
   print(reverseStringSlicing(s))


""" second method: Two pointer  """
def reverseStringLoop(s):
   char = list(s)
   left , right = 0, len(char) - 1
   while left < right:
      char[left], char[right] = char[right], char[left]
      left += 1
      right -= 1
   return "".join(char)
if __name__ == "__main__":
   s = input("Enter a string: ")
   print(reverseStringLoop(s))


""" third method :by using stack  """
def reverseStringStack(s):
   stack = list(s)
   reverse_str = ""
   while stack:
      reverse_str += stack.pop()
   return reverse_str
if __name__ == "__main__":
   s = input("Enter a string: ")
   print(reverseStringStack(s))