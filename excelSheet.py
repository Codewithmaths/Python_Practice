""" find the number of the excel sheet with the columntitle """
class TitleToNumber:
   def titleToNumber(columnTitle):
      result = 0
      for i in columnTitle:
         value = ord(i) - ord('A') + 1
         result = result * 26 + value
      return result 
if __name__ == "__main__":
   columnTitle = input("Enter the column title: ")
   print(TitleToNumber.titleToNumber(columnTitle))


""" find the excel sheet column title with the number """
class NumberToTitle:
   def numberToTitle(num):
      result = []
      while num > 0:
         num -= 1
         char = chr(num %26 + ord('A'))
         result .append(char)
         num //= 26
      return "".join(result[::-1])
if __name__ == "__main__":
   num = int(input("Enter the number: "))
   print(NumberToTitle.numberToTitle(num))

