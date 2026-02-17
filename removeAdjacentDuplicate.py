""" Remove the adjacent duplicate characters in a string. """
class RemoveAdjacentDuplicate:
   def removeAdjacentDuplicate(self, s):
      stack = []
      for char in s:
         if stack and stack[-1] == char:
            stack.pop()
         else:
            stack.append(char)
      return ''.join(stack)
if __name__ == "__main__":
   s = input("Enter a string: ")
   RAD = RemoveAdjacentDuplicate()
   print(RAD.removeAdjacentDuplicate(s))