class Solution:
    @staticmethod
    def helper(nums, subsets, curr, i, end):
        if i == end:
            subsets.append(curr.copy())
            return

        curr.append(nums[i])
        Solution.helper(nums, subsets, curr.copy(), i+1, end)
        curr.pop()
        Solution.helper(nums, subsets, curr.copy(), i+1, end)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets: List[List[int]] = []
        current: List[int] = []
        i = 0
        end = len(nums)
        Solution.helper(nums, subsets, current, i, end)
        return subsets
