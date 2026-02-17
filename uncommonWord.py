""" uncommon word """
from typing import Counter
class UncommonWord:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        all_word = s1.split() + s2.split()
        count = Counter(all_word)
        return [word for word in count if count[word] == 1]
if __name__ == "__main__":
    s1 = input("Enter the first sentence: ")
   #  s1 = [i.strip() for i in s1]
    s2 = input("Enter the second sentence: ")
   #  s2 = [i.strip() for i in s2]
   # s1 = "this apple is sweet"
   # s2 = "this apple is sour"
    print(UncommonWord().uncommonFromSentences(s1, s2))
