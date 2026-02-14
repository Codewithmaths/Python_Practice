# a = int(input("enter first number :"))
# b = int(input("enter second number :"))
# def avgOfTwo(a,b):
#     avg = (a+b)/2
#     print(avg)
#     # return avg
# avgOfTwo(a,b)

# def avgs(* numbers):
#     sum = 0
#     for i in numbers:
#         sum = sum +i
#     print(f"Avg of {numbers} is {sum/len(numbers)}")
#     return sum/len(numbers)
# print(avgs(1,3,5))


# a = int(input("enter a number :"))
# b = int(input("enter a number :"))
# c = int(input("enter a number :"))
# d = int(input("enter a number :"))
# e = int(input("enter a number :"))
# f = int(input("enter a number :"))
# s =set()
# s.add(a)
# s.add(b)
# s.add(c)
# s.add(d)
# s.add(e)
# s.add(f)
# print(s)
# s={}
# s.update({"manav":"python"})
# s.update({"manav":"java"})
# s.update({"mana":"python"})
# s.update({"mv":"java"})
# print(s)

# s={8,7,12,"harry",[1,2]}
# print(s)

""" print 0 to 50 numbers """
# i = 0 
# while i < 51 :
#     print(i)
#     i +=1


# l = [1,2,3]
# item = 0
# for item in l :
#     print(item)


# l1=["Harry","Soham","Sachin","Rahul"]
# name =[]
# for i in l1:
#     print(i)
#     name.append(i.startswith)
# print(name)

""" Sum Upto given input """
# num= int(input("enter number :"))
# sum =0
# i=0
# while i<(num + 1) :
#     sum =sum + i
#     i+=1
#     # print(sum)
# print(f"sum of{num} is {sum}")
   

# nums = int(input("enter number :"))
# for i in range(nums):
#     print("*")
#     for j in range(1,i+2):
#         print("*")
                
""" function for greeting code """
# def func1(name):
#     print(f"good day {name}")
# func1("manav")

""" function for factorial for given input """
# def factorial(n):
#     i=0,1
#     if i==0 or i==1:
#         return 1
#     else:
#         return n*factorial(n-1)
# factorial(5)

""" using os modules read the file """
# import os 
# f = open("C:/Manav/Home/practical_sem4/AAD/AAD_pract.txt","r")
# text = f.read()
# print(text)
# f.close

""" usinng OS module write inthe file """
# import os 
# f = open("C:/Manav/Home/practical_sem4/AAD/table_pract.txt","w")
# f.write("2 4 6 8 10 12 14 16 18 20 22 24 26 ")
# f.close


# import os
# with open("C:/Manav/Home/practical_sem4/AAD/AAD_pract.txt")as f:
#     f.read()


# class Programmer:
#     def __init__(self,name,company):
#         self.name = name
#         self.company = company
#     def __str__(self):
#         return f"{self.name},{self.company}"
# p = Programmer("manav","google")
# print(p)


# from math import sqrt
# class solve():
#     def __init__(self,n) -> None:
#         self.n = n
#     def sq(n):
#         return n*n
#     def cube(n):
#         return n*n*n
#     def sqrt(n):
#         return sqrt(n)
#     def __repr__(self) -> str:
#         return sq,sqrt,cube
# s = solve(n)
# print(s)


# list=[5,10,12,13,14,15,20,25]
# def mutliOfFive(n):
#     return n/5 ==0
# list1 = filter(mutliOfFive,list)
# print(list1)
 

# List = [character for character in [1, 2, 3]] 
# print(List)


# string = 'Geeks4Geeks'
# List = list(map(lambda i: chr(ord(i) ^ 32), string)) 
# print(List) 

""" function for sum the digit of given number """
# def digitSum(n): 
#     dsum = 0
#     for ele in str(n): 
#         dsum += int(ele) 
#     return dsum 
# d=digitSum(1235)
# print(d)

""" lambda function for reemove the digit frm the given string """
# filter_nums = lambda s: ''.join([ch for ch in s if not ch.isdigit()])
# print("filter_nums():", filter_nums("101Geeks101"))

""" using lambda function for give the greater number from the given number of input """
# import functools
# lis= [1, 9, 5, 6, 11] 
# print("The maximum element of the list is : ", end="") 
# print(functools.reduce(lambda a, b: a if a > b else b, lis)) 


# for i in range(1001):
#     print(i)

""" fibonacci series """
# def recursive_fibo(n):
#     if n<=1:
#         return n 
#     else :
#         return (recursive_fibo(n-1)+recursive_fibo(n-2))
# terms = int(input("enter any number"))
# print(recursive_fibo(terms))
# if terms <= 0:
#     print("invalide input! please inpute a positive interger number")
# else :
#     print("fibonacci series : ")
# for i in range(terms):
#     print(recursive_fibo(i))

""" factorial """
# def recursive_factorial(n):
#     if n==1:
#         return n
#     else:
#         return n*recursive_factorial(n-1)
# nums= int(input("enter number :"))
# if nums < 0 :
#     print("invalide input !")
# elif nums==0:
#     print("factorial of number o is 0 ")
# else:
#     print("factorisl of number",nums,"=",recursive_factorial(nums))

""" factorial """
# def recursive_factor(n):
#     if (n==0):
#         return 1
#     return n*recursive_factor(n-1)
# nums= int(input("enter number :"))
# print(recursive_factor(nums))

""" factorial with tail recursive """
# def recusive_facto(n,a=1):
#     if (n==0):
#         return a
#     return recusive_facto(n-1,n*a)
# nums = int(input("enter numbers :"))
# print(recusive_facto(nums))

"""Guess The Correct Number"""
# import random
# num2 = random.randint(1,100)
# print(num2)
# attempts =0
# while True:
#     try:
#         num1 = int(input("Enter your number :"))
#         attempts +=1
#         if num1>num2:
#             print("come to less")
#         elif num1<num2:
#             print("thing high")
#         else:
#             print(f"correct ,you win at {attempts} attempts")
#             break
#     except ValueError:
#         print("invalide number")

""" Regular Expression """

# import re 
# s = 'geeks.forgeeks' 
# match = re.search(r's', s) 
# print(match)
# match = re.search(r'\.', s) 
# print(match) 

# import re 
# string = "manav singh"
# pattern = "[a-m]"
# result = re.findall(pattern, string) 
# print(result)
# p = re.compile('\W') 
# print(p.findall("he said *** in some_language.")) 

# import re
# s="Welcome to GeeksForGeeks"
# res=re.search(r"\bGee",s)
# print(res)
# print(res.re)
# print(res.string)

# print(res.start())
# print(res.end())
# print(res.span())

# import re
# s="Welcome to GeeksForGeeks"
# res=re.search(r"\D{2} t",s)
# print(res.group())

 
# import re  
# def findMonthAndDate(string): 
# 	regex = r"([a-zA-Z]+) (\d+)"
# 	match = re.match(regex, string) 
# 	if match == None: 
# 		print ("Not a valid date") 
# 		return
# 	print ("Given Data: %s" % (match.group())) 
# 	print ("Month: %s" % (match.group(1))) 
# 	print ("Day: %s" % (match.group(2))) 
# findMonthAndDate("Jun 24") 
# print("") 
# findMonthAndDate("I was born on June 24")

"""Extrac email from given text """
# import re
# text = "manav@qmail.com how are you ,you are shiva@ymail.com"
# new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", text, re.I))
# print(new_emails)

# import re
# regex = r'^[a-z]$|^([a-z]).*\1$'
# def check(string):
#     if(re.search(regex, string)):  
#         print("Valid")  
#     else:  
#         print("Invalid")  
# if __name__ == '__main__' :
#     sample1 = "abba"
#     sample2 = "a"
#     sample3 = "abcd"
#     check(sample1)
#     check(sample2)
#     check(sample3)

# def func(obj):
# 	obj.capital()
# 	obj.language()
# 	obj.type()
# obj_ind = India()
# obj_usa = USA()
# func(obj_ind)
# func(obj_usa)

"""Accessing private class outside the class"""
# class MyClass:
#     __hiddenVariable=10
# obj = MyClass()
# print(obj._MyClass__hiddenVariable)

""" Where RCb win """
# from random import randrange
# teams =["RCB","CSk","MI","RR","KKR","GT","LSG","PSKB","SRH","DC"]
# trophy = randrange(0,len(teams))
# print(f"{teams[trophy]} won ")

"""iter and __next__() method"""
# name= ["Manav Singh","ruby singh","mannu singh","rishi","shiva","ankit","adi","ankit","aadarsh","power","ultimate"]
# name= iter(name)
# print(name)
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))
# print(next(name))

"""can iteratable or not """
# def it(ob):
#     try:
#         iter(ob)
#         return True
#     except TypeError:
# 	    return False
# for i in [34, [4, 5], (4, 5),{"a":4}, "dfsdf", 4.5]:
#     print(i,"is iterable :",it(i))

"""counter function """
# class Counter:
# 	def __init__(self, start, end):
# 		self.num = start
# 		self.end = end

# 	def __iter__(self):
# 		return self

# 	def __next__(self): 
# 		if self.num > self.end:
# 			raise StopIteration
# 		else:
# 			self.num += 1
# 			return self.num - 1
						
# # Driver code
# if __name__ == '__main__' :
# 	a, b = 2, 5
# 	c1 = Counter(a, b)
# 	c2 = Counter(a, b)
	
# 	# Way 1-to print the range without iter()
# 	print ("Print the range without iter()")
	
# 	for i in c1:
# 		print ("Eating more Pizzas, counting ", i, end ="\n")
	
# 	print ("\nPrint the range using iter()\n")
	
# 	# Way 2- using iter()
# 	obj = iter(c2)
# 	try:
# 		while True: # Print till error raised
# 			print ("Eating more Pizzas, counting ", next(obj))
# 	except: 
# 		# when StopIteration raised, Print custom message
# 		print ("\nDead on overfood, GAME OVER") 


""" A simple generator for Fibonacci Numbers""" 
# def fib(limit): 
# 	# Initialize first two Fibonacci Numbers 
# 	a, b = 0, 1
# 	# One by one yield next Fibonacci Number 
# 	while a < limit: 
# 		yield a 
# 		a, b = b, a + b 
# # Create a generator object 
# x = fib(100) 
# # Iterating over the generator object using for 
# # in loop. 
# print("\nUsing for in loop") 
# for i in fib(100): 
# 	print(i)
		#using _next__()
# print(next(x)) 
# print(next(x)) 
# print(next(x)) 
# print(next(x)) 
# print(next(x)) 
# print(next(x)) 

# Generator_exp=(i*5 for i in range(5) if i%2==0)
# for i in Generator_exp:
#     print(i)

""" Garbage Collector """
# import gc 
# gc.disable()
# gc.enable()
# gc.collect()
# thresholds=gc.get_threshold()
# print(thresholds)

""" pytest """
class Add:
    def add(x, y):
        return x + y
class Sub:
    def subtract(x, y):
        return x - y


""" Calculator """
# a=int(input("Enter first number:"))
# b=int(input("Enter second number:"))
# class calculator:
#     def add(self,a,b):
#         return a+b
#     def sub(self,a,b):
#         return a-b
#     def multipy(self,a,b):
#         return a*b
#     def divide(self,a,b):
#         if b==0:
#             raise ValueError("divide by zero")
#         return a/b
# cal=calculator()
# print(cal.add(a,b))
# print(cal.sub(a,b))
# print(cal.multipy(a,b))
# print(cal.divide(a,b))


# def multiple_test_cases(number):
#     '''
#     This function checks multiple test cases for a given number.
#     Define input and expected output:
#     >>> multiple_test_cases(0)
#     'Zero'
#     >>> multiple_test_cases(5)
#     'Positive'
#     >>> multiple_test_cases(-5)
#     'Negative'
#     >>> multiple_test_cases(100)
#     'Large positive'
#     >>> multiple_test_cases(-100)
#     'Large negative'
#     '''
#     if number == 0:
#         return 'Zero'
#     elif number > 0:
#         if number > 10:
#             return 'Large positive'
#         else:
#             return 'Positive'
#     else:
#         if number < -10:
#             return 'Large negative'
#         else:
#             return 'Negative'

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod(verbose=True)

# '''practice_2.py module'''
# class Algebra:
# 	def square(x):
# 		return x**2
# 	def cube(x):
# 		return x**3
# class Geometry:
# 	def is_triangle(a, b, c):
# 		return a + b + c == 180
# 	def is_quadrilateral(w, x, y, z):
# 		return w + x + y + z == 360

