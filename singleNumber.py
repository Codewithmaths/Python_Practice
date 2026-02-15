""" Single Number: Given a non-empty array of integers, every element appears twice except for one. Find that single one. """

""" Single Number by using XOR operator: The XOR operator (^) returns 0 when two bits are the same and 1 when they are different. Therefore, if we XOR all the numbers in the array, the pairs of duplicate numbers will cancel each other out, leaving us with the single number that appears only once. """
def single_number(nums):
   result = 0
   for num in nums:
      result ^= num
   return result
if __name__ == "__main__":
   nums = [4, 1, 2, 1, 2]
   print(single_number(nums)) #