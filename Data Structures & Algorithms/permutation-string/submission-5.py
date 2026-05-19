class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)): return False
        target = [0]*26
        window = [0]*26

        for i in range(len(s1)):
            target[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        if target == window:
            return True

        left = 0
        for right in range(len(s1), len(s2)):
            window[ord(s2[right]) - ord('a')] += 1
            window[ord(s2[left]) - ord('a')] -= 1
            left += 1
            if window == target:
                return True
        return False
