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


""" optimized version of the above code """
def find_smallest_elements(nums):
    if len(nums) < 2:
        return "Array must have at least two elements"

    # Initialize with a very large number
    small = float('inf')
    second_small = float('inf')

    for n in nums:
        if n < small:
            # The current smallest becomes the second smallest
            second_small = small
            small = n
        elif n < second_small and n != small:
            # Found a new second smallest
            second_small = n

    if second_small == float('inf'):
        return "No second smallest element found (all elements might be same)"
    
    return small, second_small
if __name__ == "__main__":
    nums  = input("Enter your list by separating number with commas:").split(',')
    nums = [float(i.strip()) for i in nums]
    result = find_smallest_elements(nums)
    if isinstance(result, tuple):
        print("Smallest:", result[0], "Second Smallest:", result[1])
    else:
        print(result)