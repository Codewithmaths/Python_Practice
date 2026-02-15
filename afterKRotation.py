""" After K Rotation """


""" First method using slicing """
def rotate(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums
if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    k = 2
    print(rotate(nums, k))


""" Second method using reverse """
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1
def rotate_inplace(nums, k):
    n = len(nums)
    k %= n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)
    return nums   
if __name__ == "__main__":
      nums = [1, 2, 3, 4, 5]
      k = 2
      print(rotate_inplace(nums, k))   
      