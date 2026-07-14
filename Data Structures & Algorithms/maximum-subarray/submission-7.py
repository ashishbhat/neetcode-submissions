class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = ans = nums[0]
        l = 0

        for r in range(1, len(nums)):
            if curr < 0:
                curr = nums[r]
            else:
                curr = curr + nums[r]
            if curr > ans:
                ans = curr
        return ans

    
