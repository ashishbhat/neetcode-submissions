class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = []
        current: List[int] = []
        nums.sort()

        def helper(i, total):
            if i == len(nums):
                subsets.append(current.copy())
                return

            current.append(nums[i])
            helper(i+1, total + nums[i])

            current.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i += 1
            helper(i+1, total)

        helper(0, 0)
        return subsets