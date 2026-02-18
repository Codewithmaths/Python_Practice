""" count the binary substring """
def count_binary_substrings(s):
   count = 0
   prev = 0
   curr = 1
   for i in range(1, len(s)):
      if s[i] == s[i - 1]:
         curr += 1
      else:
         count += min(prev, curr)
         prev = curr
         curr = 1
   return count + min(prev, curr)
if __name__ == "__main__":
   s = input("Enter a string of 0s and 1s: ")
   print(count_binary_substrings(s))
   