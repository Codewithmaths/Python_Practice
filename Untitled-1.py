# for i in range(1, 6):  # Loop from 1 to 5 (inclusive)
#     print(chr(96 + i) * i)  # Print the character i times
#     print(chr(64 + i) * i) # Capital alphabet

# """ Calculator Function """
# def calculate_equation(expression):
#     try:
#         result = eval(expression)
#         return result
#     except Exception as e:
#         return f"Error: {e}"

# print(calculate_equation("2 + 3 * 4"))
# print(calculate_equation("(5 - 1) / 2"))
# print(calculate_equation("10 / 0"))     

# """  """


x = [5,6,7,8]
x.insert(2, 0) 
print(x) # Insert 10 at index 2