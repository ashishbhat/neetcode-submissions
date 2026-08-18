from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n1 = len(s)
        n2 = len(p)

        @cache
        def dfs(i: int, j: int) -> bool:
            print(i,j)
            # if pattern is exhausted but string is not
            if j == n2 and i < n1:
                return False
            # if both are exhausted
            if i == n1 and j == n2:
                return True


            match = i < n1 and (s[i] == p[j] or p[j] == ".")
            
            if j+1 < n2 and p[j+1] == "*":
                return dfs(i, j+2) or (match and dfs(i+1, j))
            
            if match:
                return dfs(i+1, j+1)

            return False
            
                
           
        return dfs(0,0)
