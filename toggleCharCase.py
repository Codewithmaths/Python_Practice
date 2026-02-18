""" toggle the case of each character in a string """
def toggleCase(str):
   result = ""
   for i in str:
      if i.upper() == i:
         result += i.lower() 
      else:
         result += i.upper()
   return result 
if __name__ == "__main__":
   str = input("Enter a string: ")
   print(toggleCase(str))


""" second method: swapcase"""
def toogleCharSwapcase(str):
   return str.swapcase()
if __name__ == "__main__":
   str = input("Enter a string: ")
   print(toogleCharSwapcase(str))


""" third method : ASCII """
def toggleCharAscii(s):
   res = ""
   for char in s:
      val = ord(char)
      if 65 <= val <= 90:
         res += chr(val + 32)
      elif 97 <= val <=122:
         res += chr(val - 32)
      else:
         res += char
   return res
if __name__ == "__main__":
   s = input("Enter a string: ")
   print(toggleCharAscii(s))
