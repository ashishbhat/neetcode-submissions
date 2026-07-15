class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        x = []
        def helper():
            if len(x) == len(nums):
                result.append(x.copy())
                return

            for i in nums:
                if i not in visited:
                    visited.add(i)
                    x.append(i)
                    helper()
                    x.pop()
                    visited.remove(i)
        helper()
        return result