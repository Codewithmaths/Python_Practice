""" checking the another string present in the main strinf or not  """


""" first method """
def checkSubString(str1, str2):
   if str2 in str1:
      return True
   return -1
if __name__ == "__main__":
   str1 = input("Enter the main string: ")
   str2 = input("Enter the sub string: ")
   print(checkSubString(str1, str2))


""" second method : USING find() function"""
def checkSubStringFind(str1, str2):
   idx = str1.find(str2)
   print(idx)
if __name__ == "__main__":
   str1 = input("enter you string:")
   str2 = input("enter sub string:")
   checkSubStringFind(str1, str2)


""" third method: """
def manual_substring_check(main, sub):
    n, m = len(main), len(sub)
    
    # We only need to loop until the remaining main string is shorter than sub
    for i in range(n - m + 1):
        # Check the window of length m
        if main[i : i + m] == sub:
            return i
    return -1
if __name__ == "__main__":
   main = input("Enter the main string: ")
   sub = input("Enter the sub string: ") 
   print(manual_substring_check(main, sub))
