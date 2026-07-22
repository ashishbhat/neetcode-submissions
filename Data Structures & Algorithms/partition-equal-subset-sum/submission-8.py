class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        T = sum(nums)
        if T % 2 == 1:
            return False
        N = len(nums)
        T = T//2

        dp = [False] * (T+1)
        dp[0] = True

        for current in nums:
            for j in range(T, -1, -1):
                if j >= current:
                    dp[j] = dp[j - current] or dp[j]
                else:
                    dp[j] = dp[j]
        print(dp)
        return dp[T]
