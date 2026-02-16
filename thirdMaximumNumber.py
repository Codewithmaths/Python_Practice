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
def thirdMaximumNumber(nums):
   nums = list(set(nums))
   if len(nums) >= 3:
      return nums[-3]
   return nums[-1]
if __name__ == "__main__":
   nums = input("Enter a list of numbers separated by commas: ").split(',')
   nums = [int(i.strip()) for i in nums]
   print(thirdMaximumNumber(nums))


""" third method """
def third_max(nums):
   first = second = third = float('-inf')
   uni_nums = set(nums)
   if len(uni_nums) < 3:
      return max(uni_nums)
   for n in uni_nums:
      if n > first:
         third = second
         second = first
         first = n
      elif n > second:
         third = second
         second = n
      elif n > third:
         third = n
   return third 
if __name__ == "__main__":
   nums = input("Enter a list of numbers separated by commas: ").split(',')
   nums = [int(i.strip()) for i in nums]
   print(third_max(nums))