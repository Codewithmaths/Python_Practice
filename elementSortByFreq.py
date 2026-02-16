""" sort elements by frequency. """
import re
from typing import Counter
def sort_by_freq(arr):
   freq = Counter(arr)
   arr.sort(key = lambda x: (-freq[x],x))
   return arr
if __name__ == "__main__":
   arr = input("Enter a list of elements separated by commas: ").split(',')
   arr = [int(i.strip()) for i in arr]
   print(sort_by_freq(arr))