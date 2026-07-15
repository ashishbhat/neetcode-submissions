class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = set()
        current = []

        def backtrack(i):
            total = sum(current)
            if total > target or i == len(nums):
                return
            if total == target:
                subsets.add(tuple(current.copy()))
                return


            current.append(nums[i])
            backtrack(i+1)

            backtrack(i)

            current.pop()
            backtrack(i+1)

        backtrack(0)
        return [list(x) for x in subsets]