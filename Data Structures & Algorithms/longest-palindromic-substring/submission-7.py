class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(s: str, l, r) -> (int, int):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1

            return l+1, r-1

        left_best = 0
        right_best = 0

        if len(s) == 1:
            return s

        for i in range(len(s)):
            l1 , r1 = expand(s, i, i)
            if r1 - l1 > right_best - left_best:
                left_best, right_best = l1, r1

            l2, r2 = expand(s, i, i+1)
            if r2 - l2 > right_best - left_best:
                left_best, right_best = l2, r2
        
        return s[left_best:right_best+1]
