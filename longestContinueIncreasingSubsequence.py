""" find the longest continue increasing subsequence in a list of integers"""
def longest_continue_increasing_subsequence(nums):
   if not nums:
      return 0
   max_len = 1
   curr_len = 1
   for i in range(1,len(nums)):
      if nums[i] > nums[i-1]:
         curr_len += 1
         max_len = max(max_len,curr_len)
      else:
         curr_len = 1
   return max_len
if __name__ == "__main__":
   nums = input("Enter a list of integers seperated by commas:").split(",")
   nums = [int(i.strip()) for i in nums]
   print(longest_continue_increasing_subsequence(nums))

