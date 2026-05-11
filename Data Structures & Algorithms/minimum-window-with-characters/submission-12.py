class Solution:
    def minWindow(self, s: str, t: str) -> tuple:
        target = Counter(t)
        window = defaultdict()
        left = 0
        l = 0
        r = len(s)
        have = 0
        need = len(target)
        found = False

        for right in range(len(s)):
            window[s[right]] = window.get(s[right], 0) + 1
            if window[s[right]] == target[s[right]]:
                have += 1
            if have == need:
                found = True
                while s[left] not in target or window[s[left]] > target[s[left]]:
                    window[s[left]] -= 1
                    left += 1
                if  right - left  < r - l:
                        r, l = right, left
        return s[l:r+1] if found else ""


            
            
            