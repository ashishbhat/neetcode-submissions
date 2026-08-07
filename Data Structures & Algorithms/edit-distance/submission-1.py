class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = {}

        def operations(i: int, j: int):
            if  (i,j) in dp:
                return dp[(i,j)]
                
            if j == n2:
                return n1 - i
            elif i == n1:
                return n2 - j
            
            if word1[i] == word2[j]:
                dp[(i,j)] = operations(i+1, j+1)
                return dp[(i,j)]
            else:
                dp[(i,j)] = 1 + min(
                    operations(i+1, j),
                    operations(i+1, j+1),
                    operations(i, j+1)
                    )
                return dp[(i,j)]
        ops = operations(0, 0)
        return ops