class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        subsets: List[List[int]] = []
        current: List[int] = []
        candidates.sort()

        def helper(i, total):
            if total == target:
                subsets.append(current.copy())
                return

            if total > target or i == len(candidates):
                return

            current.append(candidates[i])
            helper(i+1, total + candidates[i])

            current.pop()
            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            helper(i+1, total)

        helper(0, 0)
        return subsets
