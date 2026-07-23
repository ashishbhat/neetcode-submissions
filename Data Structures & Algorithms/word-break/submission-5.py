class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        dp = {}
        def rec(w: str):
            if w in dp:
                return dp[w]
            if w == "":
                return True
            
            res = False
            for i in range(len(w)):
                if w[0:i+1] in words:
                    res |= rec(w[i+1:])
            dp[w] = res
            return res

        return rec(s)