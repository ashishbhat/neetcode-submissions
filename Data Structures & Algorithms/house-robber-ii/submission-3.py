class Solution:
    def rob_line(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        max_robbery = [0]*len(nums)
        max_robbery[0] = nums[0]
        max_robbery[1] = max(nums[0], nums[1])

        for house in range(2, len(nums)):
            max_robbery[house] = max(
                max_robbery[house - 1],
                nums[house] + max_robbery[house - 2],
            )

        return max_robbery[-1]

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        return max(self.rob_line(nums[0:n-1]), self.rob_line(nums[1:n]))
        