""" Majority Element is the element that appears more than n/2 times in the array."""


""" first approach: using a dictionary to count the occurrences of each element. """
def majorityElement(nums):
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    for key, value in count.items():
        if value > len(nums) // 2:
            return key
if __name__ == "__main__":
    nums = input("Enter a list of numbers separated by commas: ").split(',')
    nums = [int(i.strip()) for i in nums]
    print("Majority Element:", majorityElement(nums))


""" second approach: using the Boyer-Moore Voting Algorithm. """
def majorityEle(nums):
    candidate = None
    count = 0
    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    if nums.count(candidate) > len(nums) // 2:
        return candidate
    return None
if __name__ == "__main__":
      nums = input("Enter a list of numbers separated by commas: ").split(',')
      nums = [int(i.strip()) for i in nums]
      print("Majority Element:", majorityEle(nums))


""" third approach: using the built-in max function with a key argument. """
from typing import Counter
def majorEle(nums):
    count = Counter(nums)
    return max(count.keys(),key=count.get)
if __name__ == "__main__":
      nums = input("Enter a list of numbers separated by commas: ").split(',')
      nums = [int(i.strip()) for i in nums]
      print("Majority Element:", majorEle(nums))