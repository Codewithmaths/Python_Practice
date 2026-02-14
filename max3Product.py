""" Max 3 Product of 3 numbers in an array
Given an array of integers, find the maximum product of any three numbers in the array."""

def max_product_of_three(nums):
   nums.sort()
   return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])
if __name__ == "__main__":
    nums = [1, 10, 2, 6, 5, 3]
    print(max_product_of_three(nums))