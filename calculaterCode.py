a = int(input("Enter first number: "))
c = int(input("Enter second number:"))
b = input("Enter an operator: ")

match b:
    case "+": print(a + c)
    case "-": print(a - c)
    case "*": print(a * c)
    case "/": print(a / c)
    case "%": print(a % c)
    case _: print("Invalid operator")
