""" sorting the string """


""" first method """
class SortString:
   def sort_string(self, s):
      return "".join(sorted(s))

if __name__ == "__main__":
   s = input("Enter a string: ")
   sorter = SortString()
   print(sorter.sort_string(s))


""" second method """
def sortString(s):
   s = list(s)
   s.sort()
   return "".join(s)

if __name__ == "__main__":
   s = input("Enter a string: ")
   print(sortString(s))


""" third method """
class CountingSortString:
   def countindSortString(self,s):
      freq = [0] * 26
      for char in s:
         freq[ord(char) - ord('a')] += 1
      result  = []
      for i in range(26):
         result.append(chr(i + ord('a')) * freq[i])
      return "".join(result)
if __name__ == "__main__":
   s = input("Enter a string: ")
   sorter = CountingSortString()
   print(sorter.countindSortString(s))

