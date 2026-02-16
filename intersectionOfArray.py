""" find the intersection of two arrays """


"""first solution: using set intersection"""
def intersection(nums1, nums2):
   return list(set(nums1) & set(nums2))
if __name__ == "__main__":
   nums1 = input("Enter the first list of numbers separated by commas: ").split(',')
   nums1 = [int(i.strip()) for i in nums1]
   nums2 = input("Enter the second list of numbers separated by commas: ").split(',')
   nums2 = [int(i.strip()) for i in nums2]
   print("Intersection:", intersection(nums1, nums2))


"""second solution: using list comprehension"""
def intersection(nums1, nums2):
   return [i for i in nums1 if i in nums2]
if __name__ == "__main__":
   nums1 = input("Enter the first list of numbers separated by commas: ").split(',')
   nums1 = [int(i.strip()) for i in nums1]
   nums2 = input("Enter the second list of numbers separated by commas: ").split(',')
   nums2 = [int(i.strip()) for i in nums2]
   print("Intersection:", intersection(nums1, nums2))


""" Third solution: Handling duplicates """
import re
from typing import Counter
def intersection(nums1, nums2):
   c1 = Counter(nums1)
   c2 = Counter(nums2)
   result = []
   for i in nums1:
      if i in nums2:
         count = min(c1[i],c2[i])
         result.extend([i]*count)
   return result
if __name__ == "__main__":
   nums1 = input("Enter the first list of numbers separated by commas: ").split(',')
   nums1 = [int(i.strip()) for i in nums1]
   nums2 = input("Enter the second list of numbers separated by commas: ").split(',')
   nums2 = [int(i.strip()) for i in nums2]
   print("Intersection:", intersection(nums1, nums2))


""" Fouth approach:Two pointerns"""
def intersection(nums1, nums2):
   nums1.sort()
   nums2.sort()
   i, j = 0, 0
   result = []
   while i < len(nums1) and j < len(nums2):
      if nums1[i] == nums2[j]:
         result.append(nums1[i])
         i += 1
         j += 1
      elif nums1[i] < nums2[j]:
         i += 1
      else:
         j += 1
   return result
if __name__ == "__main__":
   nums1 = input("Enter the first list of numbers separated by commas: ").split(',')
   nums1 = [int(i.strip()) for i in nums1]
   nums2 = input("Enter the second list of numbers separated by commas: ").split(',')
   nums2 = [int(i.strip()) for i in nums2]
   print("Intersection:", intersection(nums1, nums2))