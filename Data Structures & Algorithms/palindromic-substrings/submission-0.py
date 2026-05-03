class Solution:
    def isPlaindrome(self, s: str, start: int, end: int) -> int:

        while start <= end - 1:
            if s[start] != s[end]:
                return 0
            start += 1
            end -= 1
        return 1


    def countSubstrings(self, s: str) -> int:
        N = len(s)
        count = 0

        for i in range(N):
            for j in range(N - i):
                count += self.isPlaindrome(s, i, i+j)
        return count

