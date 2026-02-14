""" Sum of elements in an array """

""" Sum of elements in an array """
def sum_of_array(arr):
   total = 0
   for num in arr:
      total += num
   return total
if __name__ == "__main__":
   # arr = input("Enter the elements of the array separated by space: ").split()
   # arr = [int(num) for num in arr]
   arr = [1, 2, 3, 4, 5]
   print(sum_of_array(arr))
