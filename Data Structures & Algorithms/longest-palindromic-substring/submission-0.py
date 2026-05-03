class Solution:
    def expand(self, s: str, left: int, right: int) -> tuple:
        n = 0
        v = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            v,n = (s[left:right+1], right - left + 1) 
            left -= 1
            right += 1
        return (v,n) 

    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        pal = ""
        for i in range(len(s)):
            val1, n1 =  self.expand(s,i,i)
            val2, n2 = self.expand(s,i, i+1)

            if n1 > max(n2, max_length):
                max_length = n1
                pal = val1
            if n2 > max(n1, max_length):
                max_length = n2
                pal = val2

            
        return pal