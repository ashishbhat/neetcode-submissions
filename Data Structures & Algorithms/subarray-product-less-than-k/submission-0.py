class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        N = len(nums)
        left = 0
        count = 0
        current_prod = 1
        for right in range(len(nums)):
            current_prod *= nums[right]
            while current_prod >= k and left < len(nums):
                current_prod /= nums[left]
                left += 1
            if left <= right:
                count += right - left + 1
        return count


        