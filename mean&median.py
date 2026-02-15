""" Mean and median of a list of numbers. """

def mean(num):
   total = 0
   for i in num:
      total += i
   return total / len(num)

def median(num):
   num.sort()
   n = len(num)
   mid = n // 2
   if n % 2 == 0:
      return (num[mid -1] + num[mid])/2
   else:
      return num[mid]

if __name__ == "__main__":
   num = input("Enter a list of numbers separated by commas: ").split(',')
   num = [int(i.strip()) for i in num]
   # num = [1, 2, 3, 4, 5]
   print("Mean:", mean(num))
   print("Median:", median(num))
   

""" The PRO version of this code is available """
import statistics
num = input("Enter a list of numbers separated by commas: ").split(',')
num = [int(i.strip()) for i in num]
print("Mean:", statistics.mean(num))
print("Median:", statistics.median(num))  
