""" derect capital  """


""" first method: build in function """
def detectCapital(word):
   return word.isupper() or word.islower() or word.istitle()
if __name__ == "__main__":
   word = input("Enter a word: ")
   print(detectCapital(word))


""" second method : manual approach """
def detectCapital(word):
   capitals = 0
   for char in word:
      if 'A' <= char <= 'Z':
         capitals += 1
   if capitals == len(word) : return True
   if capitals == 0 : return True
   if capitals == 1 and 'A' <= word[0] <= 'Z': return True
   return False
if __name__ == "__main__":
   word = input("Enter a word: ")
   print(detectCapital(word)) 
