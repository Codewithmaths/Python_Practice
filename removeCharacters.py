""" Remove characters from the first string which are present in the second string"""


""" first method: Optimal approach using set """
def removeCharacterSet(str1, str2):
   remove = set(str2)
   result = ''.join([char for char in str1 if char not in remove])
   return result
if __name__ == "__main__":
   str1 = input("Enter the first string: ")
   str2 = input("Enter the second string: ")
   print(removeCharacterSet(str1, str2))


"""second method"""
def removeCharacter(str1, str2):
   for i in str2:
      while i in str1:
         itr = str1.find(i)
         str1 = str1.replace(i,"")
   return str1
if __name__ == "__main__":
   str1 = input("Enter the first string: ")
   str2 = input("Enter the second string: ")
   print(removeCharacter(str1, str2))