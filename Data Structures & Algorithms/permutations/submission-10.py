class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False] * len(nums)
        x = []
        def helper():
            if len(x) == len(nums):
                result.append(x.copy())
                return

            for j, i in enumerate(nums):
                if not visited[j]:
                    visited[j] = True
                    x.append(i)
                    helper()
                    x.pop()
                    visited[j] = False
        helper()
        return result