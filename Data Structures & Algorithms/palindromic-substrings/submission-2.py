class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(l: int, r: int) -> int:
            palindromes = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                palindromes += 1
                l -= 1
                r += 1
            return palindromes

        if len(s) == 1:
            return 1
        result = 0

        for i in range(len(s)):
            result += expand(i, i) + expand(i, i+1)
        
        return result