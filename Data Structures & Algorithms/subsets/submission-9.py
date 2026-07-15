class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = []
        current: List[int] = []

        def helper(i):
            if i == len(nums):
                subsets.append(current.copy())
                return

            current.append(nums[i])
            helper(i+1)

            current.pop()
            helper(i+1)

        helper(0)
        return subsets
