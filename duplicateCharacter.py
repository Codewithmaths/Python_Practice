""" find duplicate character in string and return char and their count """
def duplicateChar(s):
   char_count = {}
   for char in s:
      if char in char_count:
         char_count[char] += 1
      else:
         char_count[char] = 1
   for char, count in char_count.items():
      if count > 1:
         print(f"{char} : {count}")
if __name__ == "__main__":
   s = input("Enter a string: ")
   print(duplicateChar(s))


""" second method : sorting """
def duplicateCharSort(s):
   char = sorted(s)
   i = 0
   while i < len(char) - 1:
      count = 1
      while i < len(char) -1 and char[i] == char[i + 1]:
         count += 1
         i += 1
      if count > 1:
         print(f"{char[i]} : {count}")
      i += 1
if __name__== "__main__":
   s = input("Enter a string: ")
   duplicateCharSort(s) 