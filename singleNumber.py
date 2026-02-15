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

""" second method """
def single_number(nums):
   return 2 * sum(set(nums)) - sum(nums)
if __name__ == "__main__":
   nums = [4, 1, 2, 1, 2]
   print(single_number(nums)) #  


""" third method """
def single_number(nums):
   num_dict = {}
   for num in nums:
      if num in num_dict:
         del num_dict[num]
      else:
         num_dict[num] = 1
   return list(num_dict.keys())[0]
if __name__ == "__main__":
   nums = [4, 1, 2, 1, 2]
   print(single_number(nums)) # 4