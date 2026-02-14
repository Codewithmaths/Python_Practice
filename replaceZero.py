""" First method to replace all zeroes with 5 by using mathematical approach. """
def replace_zeroes(num):
    if num == 0:
        return 5

    result = 0
    multiplier = 1

    while num > 0:
        digit = num % 10
        if digit == 0:
            digit = 5
        result += digit * multiplier
        multiplier *= 10
        num //= 10

    return result
print(replace_zeroes(1020))  # Output: 1525


""" Second method to replace all zeroes with 5 by using string manipulation. """
def replace_zeroes_string(num):
    return int(str(num).replace('0', '5'))
print(replace_zeroes_string(1020))  # Output: 1525


""" Third method to replace all zeroes with 5 by using recursion. """
def replace_zeroes_recursive(num):
    if num == 0:
        return 0
    last_digit = num % 10
    if last_digit == 0:
        last_digit = 5
    return replace_zeroes_recursive(num // 10) * 10 + last_digit
print(replace_zeroes_recursive(1020))  # Output: 1525