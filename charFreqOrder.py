""" find the character frequency in order  """


""" first method using dictionary """
class CharacterFrequencyDict:
   def characterFrequencyDict(self,string):
      freq = {}
      for i in string:
         if i in freq:
            freq[i] += 1
         else:
            freq[i] = 1
      for i in string:
         if freq[i] != 0:
            print(f"{i} : {freq[i]}")
            freq[i] = 0
if __name__ == "__main__":
   string = input("Enter a string: ")
   CFD = CharacterFrequencyDict()
   print(CFD.characterFrequencyDict(string)) 


""" second method using collections module """
class CharacterFrequencyDicts:
   def characterFrequencyDicts(self,s):
      freq = {}
      for i in s:
         freq[i] = freq.get(i,0) + 1
      for i, count in freq.items():
         print(f"{i} : {count}")
if __name__ == "__main__":
   s = input("Enter a string: ")
   CFD = CharacterFrequencyDicts()
   print(CFD.characterFrequencyDicts(s))


""" third method """
def freq_manual_count(s):
   from collections import Counter
   count = Counter(s)
   visited = set()
   for i in s:
      if i not in visited:
         print(f"{i} : {count[i]}")
         visited.add(i)
if __name__ == "__main__":
   s = input("Enter a string: ")
   freq_manual_count(s)
