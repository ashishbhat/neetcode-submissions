class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1, word2 = word2, word1
        n1 = len(word1)
        n2 = len(word2)

        dp = [[0]*(n1+1) for _ in range(n2+1)]

        for i in range(n2):
            dp[i][n1] =  n2 - i
        for i in range(n1):
            dp[n2][i] = n1 - i

        for i in range(n2-1, -1, -1):
            for j in range(n1-1, -1, -1):
                if word1[j] == word2[i]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i+1][j+1],
                        dp[i][j+1],
                        dp[i+1][j]
                    )
        return dp[0][0]