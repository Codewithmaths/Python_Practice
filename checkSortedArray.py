""" check array is sorted or not """


""" check array is sorted or not by iterating through the array and comparing each element with the next one. If any element is greater than the next one, then the array is not sorted. """
def checkSortedArray(arr):
   for i in range (len(arr) - 1):
      if arr[i] > arr[i + 1]:
         return False
   return True 
if __name__ == "__main__":
   arr = [1, 2, 3, 4, 5]
   print(checkSortedArray(arr)) # True


""" check array is sorted or not by list comprehension and all() function."""
def checkSortedArrays(arr):
   return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
if __name__ == "__main__":
   arr = [1, 2, 3, 4, 10]
   print(checkSortedArrays(arr)) # True


""" check array is sorted or not by using the built-in sorted() function and comparing it with the original array. If the sorted array is the same as the original array, then the array is sorted. """
def checkSortedArrayUsingSorted(arr):
   return arr == sorted(arr)
if __name__ == "__main__":   
   arr = [1, 2, 3, 4, 5]
   print(checkSortedArrayUsingSorted(arr)) # True


""" check ascending order or descending order """
def checkSortedArrayOrder(arr):
   ascending = True 
   descending = True 
   for i in range (len(arr) - 1):
      if arr[i] > arr[i + 1]:
         ascending = False
      if arr[i] < arr[i + 1]:
         descending = False
      
      if ascending : return "Ascending order"
      if descending : return "Descending order"
      return "Not sorted"
if __name__ == "__main__":
   arr = [1, 2, 3, 4, 5]
   arr = [5, 4, 3, 2, 1]
   print(checkSortedArrayOrder(arr)) # Ascending order
