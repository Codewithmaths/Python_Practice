""" Small and second small number in a list """
def smallSecSmall(nums):
   nums.sort()
   small = nums[0]
   secondSmall = None
   for i in range(1,len(nums)):
      if nums[i] != small:
         secondSmall = nums[i]
         break
   if secondSmall is None:
      return [-1]
   return [small, secondSmall]
if __name__ == "__main__":
   nums  = input("Enter your list by separating number with commas:").split(',')
   nums = [float(i.strip()) for i in nums]
   print(smallSecSmall(nums))