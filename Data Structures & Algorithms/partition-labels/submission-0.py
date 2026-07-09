class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = Counter(s)
        current = set()
        ans = []
        left = 0

        for right in range(len(s)):
            ch = s[right]
            current.add(ch)
            freq[ch] -= 1
            if freq[ch] == 0:
                current.remove(ch)
            if not current:
                ans.append(right - left + 1)
                left = right + 1

        return ans
