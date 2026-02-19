""" check number is divisible by 13 or not """

def check_13_logic(n):
    if n < 0: n = -n
    if n == 0 or n == 13: return True
    if n < 13: return False
    
    # Apply the rule: (rest of number) + (last digit * 4)
    last_digit = n % 10
    rest_of_number = n // 10
    new_num = rest_of_number + (last_digit * 4)
    return check_13_logic(new_num)
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print(check_13_logic(n))
