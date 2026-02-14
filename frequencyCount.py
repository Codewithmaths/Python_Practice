""" Counting the frequency of elements in an array. """


""" first method using dictionary"""
def frequency_count(arr):
   frequency_count = {}
   for ele in arr:
      if ele in frequency_count:
         frequency_count[ele] += 1
      else:
         frequency_count[ele] = 1
   return frequency_count
if __name__ == "__main__":
   arr = [1, 2, 3, 4, 5, 1, 2, 3]
   print(frequency_count(arr))   


""" second method using collections module"""
import collections
from typing import Counter
def frequency_count(arr):
   freq = Counter(arr)
   return freq
if __name__ == "__main__":
   arr = [1, 2, 3, 4, 5, 1, 2, 3]
   print(frequency_count(arr))


""" third method without using extra space"""
def frequency_count(arr):
   arr.sort()
   n = len(arr)
   i = 0 
   while i < n:
      count = 1
      while i + 1 < n and arr[i] == arr[i + 1]:
         count += 1
         i += 1
         print(f"{arr[i]}: {count}")
         i += 1
if __name__ == "__main__":
   arr = [1, 2, 3, 4, 5, 1, 2, 3]
   frequency_count(arr) 
