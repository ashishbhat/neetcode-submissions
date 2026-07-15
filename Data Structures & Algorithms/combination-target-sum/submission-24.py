class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = []
        current = []
        def backtrack(i, total):
            if total > target or i == len(nums):
                return
            if total == target:
                subsets.append(current.copy())
                return


            total += nums[i]
            current.append(nums[i])
            backtrack(i, total)


            total -= current.pop()
            backtrack(i+1, total)

        backtrack(0, 0)
        return subsets