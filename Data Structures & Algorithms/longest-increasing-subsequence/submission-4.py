class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N

        for i in range(N):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        print(dp)
        return max(dp)
        
            