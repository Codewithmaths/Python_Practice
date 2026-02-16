""" find the peak element in an array, which is greater than its neighbors. """


""" first method : O(log n) time complexity, O(1) space complexity. """
def findPeakElement(nums):
   left,right = 0,len(nums)-1
   while left < right:
      mid = left + (right - left)//2
      if nums[mid] < nums[mid + 1]:
         left = mid + 1
      else:
         right = mid 
   return left 
if __name__ == "__main__":
   nums = input("Enter a list of numbers separated by commas: ").split(',')
   nums = [int(i.strip()) for i in nums]
   print(findPeakElement(nums))


""" second method : O(n) time complexity, O(1) space complexity. """
def find_peak_linear(nums):
    for i in range(len(nums)):
        # Check if i is the peak by comparing with neighbors
        is_left_smaller = (i == 0 or nums[i] > nums[i-1])
        is_right_smaller = (i == len(nums)-1 or nums[i] > nums[i+1])
        
        if is_left_smaller and is_right_smaller:
            return i
    return 0
if __name__ == "__main__":
   nums = input("Enter a list of numbers separated by commas: ").split(',')
   nums = [int(i.strip()) for i in nums]
   print(find_peak_linear(nums))