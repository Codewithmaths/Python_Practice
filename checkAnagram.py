# """ check the one string is anagram of second string  """


# """ first method """
# def checkAnagram(str1, str2):
#    if len(str1) != len(str2):
#       return False
#    return sorted(str1) == sorted(str2)
# if __name__ == "__main__":
#    str1 = input("Enter the first string: ")
#    str2 = input("Enter the second string: ")
#    print(checkAnagram(str1, str2))


# """ second method  by using the Counter (optimum method)"""
# from collections import Counter
# def checkAnagramCounter(str1, str2):
#    if len(str1) != len(str2):
#       return False
#    return Counter(str1) == Counter(str2)
# if __name__ == "__main__":
#    str1 = input("Enter the first string: ")
#    str2 = input("Enter the second string: ")
#    print(checkAnagramCounter(str1, str2))


""" third method : manual approach by using the dict """
def checkAnagramManual(str1, str2):
   if len(str1) != len(str2):
      return False
   count = {}
   for char in str1:
      count[char] = count.get(char, 0) + 1
   for char in str2:
      if char not in count or count[char] ==0:
         return False
      count[char] -= 1
   return True
if __name__ == "__main__":
   str1 = input("Enter the first string: ")
   str2 = input("Enter the second string: ")
   print(checkAnagramManual(str1, str2))


