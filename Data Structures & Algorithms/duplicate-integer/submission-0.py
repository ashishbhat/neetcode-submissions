class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for i in nums:
            if not i in seen:
                seen.add(i)
            else:
                return True
        return False