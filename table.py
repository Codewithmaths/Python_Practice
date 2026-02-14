
#Code for creating table 
a = int(input("which table you want"))
for i in range(11):
    print(f"{a}*{i}={a*i}")


"""Table using while loop"""
number = int(input("enter number which table you want :"))
i = 1
while i<11:
    print(i*number)
    i +=1
 

# Code for solving equationsS
cal =lambda: eval(input("Enter expression: "))
