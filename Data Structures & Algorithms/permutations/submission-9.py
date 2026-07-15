class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = set()
        x = []
        def helper():
            if len(x) == len(nums):
                result.append(x.copy())
                return

            for j, i in enumerate(nums):
                if j not in visited:
                    visited.add(j)
                    x.append(i)
                    helper()
                    x.pop()
                    visited.remove(j)
        helper()
        return result