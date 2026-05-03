class Solution:
    def expand(self, s: str, left: int, right: int) -> tuple:
        l = 0
        r = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            l,r = left, right 
            left -= 1
            right += 1
        return (l,r) 

    def longestPalindrome(self, s: str) -> str:
        max_length = 0
        l = r = 0
        for i in range(len(s)):
            l1, r1 =  self.expand(s,i,i)
            l2, r2 = self.expand(s,i, i+1)

            if r1 - l1 + 1> max(r2 - l2 + 1, max_length):
                max_length = r1 - l1 + 1
                l,r = l1, r1
            if r2 - l2 + 1> max(r1 - l1 + 1, max_length):
                max_length = r2 - l2 + 1
                l,r = l2, r2


            
        return s[l:r+1]