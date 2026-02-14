"""factorial using for loop"""
factNum = int(input("Enter number :"))
factorials = 1
for i in range(1,(factNum+1)):
    factorials = factorials*i

print(factorials)

"""factorial using recussive function"""

def factorial(n):
    if i==0 or i==1:
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("Enter number :"))
factorial(n)


""" factorial """
def recursive_factorial(n):
    if n==1:
        return n
    else:
        return n*recursive_factorial(n-1)
nums= int(input("enter number :"))
if nums < 0 :
    print("invalide input !")
elif nums==0:
    print("factorial of number o is 0 ")
else:
    print("factorisl of number",nums,"=",recursive_factorial(nums))



""" factorial with tail recursive """
def recusive_facto(n,a=1):
    if (n==0):
        return a
    return recusive_facto(n-1,n*a)
nums = int(input("enter numbers :"))
print(recusive_facto(nums))
