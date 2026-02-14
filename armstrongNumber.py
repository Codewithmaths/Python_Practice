""" Armstrong Number is a number that is equal to the sum of its own digits raised to the power of the number of digits. """
""" First method to check armstrong number """

def is_armstrong_num(num):
    # Convert the number to a string to easily access each digit
    num_str = str(num)
    # Get the number of digits
    num_digits = len(num_str)
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    # Return whether the sum equals the original number
    return sum_of_powers == num
print(is_armstrong_num(153))  # True
print(is_armstrong_num(9474)) # True


""" Second method to check armstrong number using mathemical approach """
def is_armstrong_number(num):
    temp = num
    count = 0
    while temp > 0:
        temp = temp // 10
        count += 1
    temp = num 
    total = 0
    while temp > 0:
        digit = temp % 10
        total += digit **count
        temp = temp // 10
    return total == num
print(is_armstrong_number(153))  # True
print(is_armstrong_number(9474)) # True


""" find the armstrong number in a given range """
def find_armstrong_numbers_in_range(start, end):
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers
print(find_armstrong_numbers_in_range(1, 10000))
