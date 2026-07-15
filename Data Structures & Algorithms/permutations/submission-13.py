class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        visited = [False] * len(nums)

        def helper(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for j, i in enumerate(nums):
                if not visited[j]:
                    visited[j] = True
                    path.append(i)
                    helper(path)
                    path.pop()
                    visited[j] = False
        helper([])
        return result