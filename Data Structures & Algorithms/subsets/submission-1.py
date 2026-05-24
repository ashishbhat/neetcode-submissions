class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        results = [] * 2**n

        def _subsets(nums, i, take, arr = None):
            if not arr:
                arr = []
            if take:
                arr.append(nums[i])
            if i == n - 1:
                results.append(arr.copy())
                return
            _subsets(nums, i+1,False, arr.copy())
            _subsets(nums, i+1,True, arr.copy())
        _subsets(nums, 0, False)
        _subsets(nums, 0, True)

        return results
