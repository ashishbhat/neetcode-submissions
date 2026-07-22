class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        if len(s) == 1:
            return 1


        dp = [0] * len(s)
        mapping = { str(i+1):chr(i + ord('A')) for i in range(26) }

        dp[0] = 1
        if s[1] == "0" and s[0:2] in mapping:
            dp[1] = 1
        elif s[1] != "0" and s[0:2] in mapping:
            dp[1] = 2
        elif s[1] != "0" and s[0:2] not in mapping:
            dp[1] = 1
        
        for i in range(2, len(s)):
            first = dp[i - 1] if s[i] != "0" else 0
            second = dp[i-2] if s[i-1:i+1] in mapping else 0
            dp[i] = first + second
        return dp[len(s)-1]