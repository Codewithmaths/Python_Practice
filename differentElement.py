""" find the different thing in the string  """

def count_all_types(s):
    vowels_list = "aeiouAEIOU"
    vowels, consonants, digits, special = 0, 0, 0, 0
    
    for char in s:
        # 1. Check if it is a letter
        if char.isalpha():
            if char in vowels_list:
                vowels += 1
            else:
                consonants += 1
        
        # 2. Check if it is a number
        elif char.isdigit():
            digits += 1
            
        # 3. Ignore spaces (usually) and count everything else as special
        elif not char.isspace():
            special += 1
            
    return {
        "Vowels": vowels,
        "Consonants": consonants,
        "Digits": digits,
        "Special": special
    }
if __name__ == "__main__":
    s = input("Enter a string: ")
    print(count_all_types(s))