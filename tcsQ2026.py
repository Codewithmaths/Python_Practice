class Solution:
    def solution(self,k,integers):
        if 1 > k > 100:
            return "Invalid input"
        if k != len(integers):
            return "Invalid input"
        sum = 0
        for i in integers:
            sum += i
        return sum
if __name__ == "__main__":
    k = int(input("Enter the value of k:"))
    integers = input("Enter the values:").split(" ")
    integers = [int(i.strip()) for i in integers]
    print(Solution().solution(k,integers))
        
