""" Contains Duplicate"""

""" first method by using set() """
def containsDuplicate(arr):
      return len(arr) != len(set(arr))
if __name__ == "__main__":
      arr = [1, 2, 3, 4, 5]
      print(containsDuplicate(arr))

""" second method by using dictionary """
def containsDuplicate(arr):
      d = {}
      for i in arr:
            if i in d:
                  return True
            else:
                  d[i] = 1
      return False
if __name__ == "__main__":
      arr = [1, 2, 3, 4, 5]
      print(containsDuplicate(arr))