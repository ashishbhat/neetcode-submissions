class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = {}
        def rec(i: int):
            if i in dp:
                return dp[i]
            if i >= len(s):
                return True
            
            res = False
            for j in range(i,len(s)):
                if s[i:j+1] in words:
                    res |= rec(j+1)
            dp[i] = res
            return res

        return rec(0)