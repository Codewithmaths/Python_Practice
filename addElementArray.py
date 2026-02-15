""" Adding element to an array """

""" Adding element to an array by using append() method """
def addElementArray(arr, element):
      arr.append(element)
      return arr
if __name__ == "__main__":
      arr = [1, 2, 3, 4]
      element = 5
      print(addElementArray(arr, element))
""" Adding element to an array by using insert() method """