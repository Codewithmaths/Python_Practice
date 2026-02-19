""" first method: Bit manupulation """
def get_power_set(s):
    n = len(s)
    power_set_size = 1 << n  # This is 2^n
    result = []

    for i in range(power_set_size):
        subset = []
        for j in range(n):
            # Check if the j-th bit of i is set to 1
            if (i & (1 << j)) > 0:
                subset.append(s[j])
        result.append(subset)
    
    return result
if __name__ == "__main__":
    s = input("Enter a string: ").split(',')
    print(get_power_set(s))


""" second method: Recursion (Backtracking) """    
def generate_subsets(index, current, s, result):
    if index == len(s):
        result.append(list(current))
        return
    
    # Choice 1: Include the element at s[index]
    current.append(s[index])
    generate_subsets(index + 1, current, s, result)
    
    # Choice 2: Exclude the element (Backtrack)
    current.pop()
    generate_subsets(index + 1, current, s, result)

if __name__ == "__main__":
    s = input("Enter a string: ").split(',')
    result = []
    generate_subsets(0, [], s, result)
    print(result)