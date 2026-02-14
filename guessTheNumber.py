import random
num2 = random.randint(1,100)
print(num2)
attempts =0
while True:
    try:
        num1 = int(input("Enter your number :"))
        attempts +=1
        if num1>num2:
            print("come to less")
        elif num1<num2:
            print("thing high")
        else:
            print(f"correct ,you win at {attempts} attempts")
            break
    except ValueError:
        print("invalide number")