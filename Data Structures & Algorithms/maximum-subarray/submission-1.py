class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(
                dp[i-1] + nums[i],
                nums[i]
            )
        return max(dp)
    
# 2  -3 4 -2 2 1 -1 4
# 2  -1 4  2 4 5  4  8