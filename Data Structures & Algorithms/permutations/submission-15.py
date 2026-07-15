class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False] * len(nums)

        def helper(path, result):
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for j, i in enumerate(nums):
                if not visited[j]:
                    visited[j] = True
                    path.append(i)
                    helper(path, result)
                    path.pop()
                    visited[j] = False
        helper([], result)
        return result