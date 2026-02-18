""" Count common subsequence in 2 strings  """
def count_common_subsequence(S,T):
   n = len(S)
   m = len(T)
   dp = [[0] * (m + 1) for _ in range(n + 1)]
   for i in range(1, n + 1):
      for j in range(1, m + 1):
         if S[i - 1] == T[j - 1]:
            dp[i][j] = dp[i -1][j] +dp[i][j - 1] + 1
         else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
   return dp[n][m]
if __name__ == "__main__":
   S = input("Enter the first string: ")
   T = input("Enter the second string: ")
   print(count_common_subsequence(S,T))