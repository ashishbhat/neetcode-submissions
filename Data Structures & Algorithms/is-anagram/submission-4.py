class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = dict()

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        for ch in t:
            if ch in freq:
                freq[ch] -= 1
                if freq[ch] == 0:
                    freq.pop(ch, None)
            else:
                return False

        if not freq:
            return True
        return False
