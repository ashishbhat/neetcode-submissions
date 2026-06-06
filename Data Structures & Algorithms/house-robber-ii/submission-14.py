class Solution:
    def rob(self, nums: List[int]) -> int:

        def rob(nums: List[int]) -> int:
            n = len(nums)
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 0:
                return 0
            dp = [0] * n

            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, n):
                dp[i] = max(
                    dp[i-2] + nums[i],
                    dp[i-1]
                )
            
            return dp[n-1]
        
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 0:
            return 0
        return max(rob(nums[:len(nums)-1]), rob(nums[1:]))
        