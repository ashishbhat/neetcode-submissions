class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 3, 4, 5]
        result = [1] * len(nums)

        prefix = 1
        for i in range(1, len(nums)):
            result[i] = prefix * nums[i-1]
            prefix = result[i]
        print(result)
        suffix = 1
        for i in range(len(nums) - 2, -1, -1):
            result[i] = result[i] * suffix * nums[i + 1]
            suffix = suffix * nums[i + 1]
        print(result)

        return result