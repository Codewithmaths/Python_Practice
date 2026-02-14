""" Two Sum Problem: Find two numbers in an array that sum to a target value. """
def two_sum(nums, target):
   num_map = {}
   for i, n in enumerate(nums):
      diff = target - n
      if diff in num_map:
         return [num_map[diff],i]
      num_map[n] = i
   return []
if __name__ == "__main__":
   nums = input("Enter a list of numbers (comma separated): ").split(",")
   target = int(input("Enter the target value: "))
   nums = [int(num.strip()) for num in nums]
   print(two_sum(nums, target))