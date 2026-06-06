class Solution:
    def longestPalindrome(self, s: str) -> str:

        def expand(s: str, l, r) -> (int, int):
            l_val, r_val = 0, 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l_val = l
                r_val = r
                l -= 1
                r += 1

            return l_val, r_val

        left_best = 0
        right_best = 0

        if len(s) == 1:
            return s

        for i in range(len(s)):
            l1 , r1 = expand(s, i, i)
            l2, r2 = expand(s, i, i+1)

            if r1 - l1 > r2 - l2 and r1 - l1 > right_best - left_best:
                left_best, right_best = l1, r1
            if r2 - l2 > r1 - l1 and r2 - l2 > right_best - left_best:
                left_best, right_best = l2, r2
        
        return s[left_best:right_best+1]
