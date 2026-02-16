""" find the third maximum number in an array """


""" first approach: sort the array and return the third element """
def third_maximum(nums):
   nums.sort(reverse=True)
   n = len(nums)
   if n < 3:
      return nums[0]
   elif n == 3:
      return nums[2]
   else:
      return nums[2]
if __name__ == "__main__":
   nums = input("Enter a list of numbers separated by commas: ").split(',')
   nums = [int(i.strip()) for i in nums]
   print(third_maximum(nums))



"""second method , using set to remove duplicates and then sort the array """
def third_maximum(nums):
   nums = list(set(nums))
   if len(nums) >= 3:
      return nums[-3]
   return nums[-1]
if __name__ == "__main__":
   nums = input("Enter a list of numbers separated by commas: ").split(',')
   nums = [int(i.strip()) for i in nums]
   print(third_maximum(nums))

