class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        seen = set()
        max_seq = 0
        for i in nums:
            if i in seen: continue
            seq = 1
            if i-1 in unique:
                max_seq = max(seq, max_seq)
                continue
            else:
                j = i + 1
                while j in unique:
                    seq += 1
                    seen.add(j)
                    j += 1
            max_seq = max(seq, max_seq)
        return max_seq


        