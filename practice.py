# x = 10 
# y =5
# print("the sum of :" ,x+y)



# x=[1,2,3]
# y=x[:]
# y.append(4)
# print(x)
# print(y)


# x ="10"
# if int(x)==10:
#     print("equal")
# else:
#     print("not equal")


# x=5
# y=x
# x=x+2
# print(y)

# x=5
# while x>0:
#     print(x)
#     x -=1

# x=5
# y=10
# z=x if x>y else y
# print(z)

# num=[1,2,3,4,5]
# sum =0
# for i in num:
#     sum +=i
# print(sum)

# num =[1,2,3,4,5]
# sq_num=[x*x for x in num]
# print(sq_num)

# for i in range(5):
#     print(i)

# num = [1,2,3,4,5,6]
# sum =0
# for i in num:
#     sum += i
#     if sum > 10 :
#         break
# print(sum)

# s="manav is a good boy"
# reverse_s=s[::-1]
# print(reverse_s)

# x =50
# y=10
# manav=x>y
# print(manav)

# num=[1,2,3,4,5]
# print(sum(num))

# import os 
# print(os.path.splitext('/path/to/file.txt'))


# import os 
# print(os.getenv('HOME'))

# import math
# print(math.radians(180))

# import random
# print(random.randint(1,10))

# def add_num(a,b,c):
#     return a+b+c
# result = add_num(1,2,3)
# print(result)

# tup =input()
# item = input()

# tup_list = tup.split(',')

# # Remove the item if it exists
# if item in tup_list:
#     tup_list.remove(item)
# else:
#     print("Item not found in tuple.")

# # Convert back to tuple
# new_tuple = tuple(tup_list)

# print(new_tuple)

# for i in range(2):
#     for j in range(i, 2):
#         print(i, j)

age = int(input("Enter your age: "))
if age >= 21:
    print("You are adult")
else:
    print("You are not adult")  