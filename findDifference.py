""" find the difference in two string """


""" first method """
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        all_ele = list(s) + list(t)
        count = Counter(all_ele)
        for i in count:
            if count[i] == 1:
                return i
            elif count[i] > 2 and count[i] % 2 == 1:
                return i
if __name__ == "__main__":
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")
    print(Solution().findTheDifference(s, t))


""" second method : By using the XOR operator""" 
def findTheDifference(s, t):
    result = 0
    for char in s:
        result ^= ord(char)
    for char in t:
        result ^= ord(char)
    return chr(result)
if __name__ == "__main__":
    s = input("Enter the first string: ")
    t = input("Enter the second string: ")
    print(findTheDifference(s, t))