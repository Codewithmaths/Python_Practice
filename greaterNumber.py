"""write a program to find greater of four numbers enters by the user"""

a = int(input("enter a number :"))
b = int(input("enter a number :"))
c = int(input("enter a number :"))
d = int(input("enter a number :"))
if(a>b):
    if(a>c):
        if(a>d):
            print(a)
        elif(a<d):
            print(d)
        else:
            print(d)
    elif(c>a):
        if(c>d):
            print(c)
        elif(d>c):
            print(d)
        else:
            print(d)
    else:
        print(a)

elif(b>a):
    if(b>c):
        if(b>d):
            print(b)
        elif(d>b):
            print(d)
        else:
            print(d)
    elif(c>b):
        if(c>d):
            print(c)
        elif(d>c):
            print(d)
        else:
            print(d)
else:
    if(a>c):
        if(a>d):
            print(a)
        elif(a<d):
            print(d)
        else:
            print(d)
    elif(c>a):
        if(c>d):
            print(c)
        elif(d>c):
            print(d)
        else:
            print(d)
    else:
        print(a)
    
""" solve """
a = int(input("enter a number :"))
b = int(input("enter a number :"))
c = int(input("enter a number :"))
d = int(input("enter a number :"))

if (a>b and a>c and a>d):
    print("Greater number is :",a)
elif(b>a and b>c and b>d):
    print("Greater number is :",b)
elif(c>a and c>b and c>d):
    print("Greater number is :",c)
else:
    print("Greater number is :",d)

    

"""best way to solve the problem"""
import functools
lis= [1, 9, 5, 6, 11] 
print("The maximum element of the list is : ", end="") 
print(functools.reduce(lambda a, b: a if a > b else b, lis)) 



