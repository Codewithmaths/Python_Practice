""" Movies zeros to the end of an array while maintaining the order of non-zero elements. """

def move_zeros(nums):
   non_zero = 0
   for i in range(len(nums)):
      if nums[i] != 0:
         nums[non_zero],nums[i] = nums[i],nums[non_zero]
         non_zero += 1
   return nums
if __name__ == "__main__":
   nums = [0, 1, 0, 3, 12]
   print(move_zeros(nums)) # Output: [1, 3, 12, 0, 0]