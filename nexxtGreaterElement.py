""" Find the next greater element for each element in the array. The next greater element for an element x is the first greater element on the right side of x in the array. If there is no greater element for x, then the next greater element for x is -1."""


""" First method """
def next_greater_element(nums1,nums2):
   result = []
   mapping = {}
   for i in nums2:
      while result and result[-1] < i:
         mapping[result.pop()] = i
      result.append(i)
   return [mapping.get(i,-1) for i in nums1]
if __name__ == "__main__":
   nums1 = input("Enter the first list of numbers separated by commas: ").split(',')
   nums2 = input("Enter the second list of numbers separated by commas: ").split(',')
   nums1 = [int(i.strip()) for i in nums1]
   nums2 = [int(i.strip()) for i in nums2]
   print(next_greater_element(nums1,nums2))


""" Second method """

   