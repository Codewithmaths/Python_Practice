""" solve the fizz buzz problem"""


""" first method """
class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        result = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 == 0:
                result.append("FizzBuzz")
            elif i % 5 == 0:
                result.append("Buzz")
            elif i % 3 == 0 :
                result.append("Fizz")
            else:
                result.append(str(i))
        return result
if __name__ == "__main__":
    n = int(input("Enter the number: "))
    print(Solution().fizzBuzz(n))