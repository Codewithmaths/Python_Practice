""" find the common characters in two strings and return them as a string """


"""first method: commom character in two strings"""
def commonCharacterSet(str1, str2):
   common = set(str1) & set(str2)
   return list(common)
if __name__ == "__main__":
   str1 = input("Enter the first string: ")
   str2 = input("Enter the second string: ")
   print(commonCharacterSet(str1, str2))


"""second method: common character in two strings"""
def commonCharacter(str1, str2):
   common = []
   for char in str1:
      if char in str2 and char not in common:
         common.append(char)
   return common
if __name__ == "__main__":
   str1 = input("Enter the first string: ")
   str2 = input("Enter the second string: ")
   print(commonCharacter(str1, str2))


""" third method : common character in list of words """
from collections import Counter
def commonCharacterList(words):
   if not words:
      return []
   res = Counter(words[0])
   for i in range(1, len(words)):
      res = res & Counter(words[i])
   return list(res.elements())
if __name__ == "__main__":
   words = input("Enter a list of words separated by space: ").split(",")
   words = [i.strip() for i in words]
   print(commonCharacterList(words))