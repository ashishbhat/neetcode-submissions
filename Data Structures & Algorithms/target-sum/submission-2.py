class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        def backtrack(i: int, total: int):
            if (i, total) in dp:
                return dp[(i, total)]

            if i == len(nums):
                return 1 if total == target else 0

            dp[(i, total)] = backtrack(i+1, total + nums[i]) + backtrack(i+1, total - nums[i])
            return dp[(i, total)]

        return backtrack(0,0) 