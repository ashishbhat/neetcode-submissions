class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        subsets = set()
        current = []
        total = 0
        def backtrack(i):
            nonlocal total
            if total > target or i == len(nums):
                return
            if total == target:
                subsets.add(tuple(current.copy()))
                return


            total += nums[i]
            current.append(nums[i])
            backtrack(i+1)

            backtrack(i)

            total -= current.pop()
            backtrack(i+1)

        backtrack(0)
        return [list(x) for x in subsets]