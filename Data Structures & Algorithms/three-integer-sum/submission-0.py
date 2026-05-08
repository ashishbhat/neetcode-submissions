class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums = sorted(nums)
        triplets: set[tuple[int]] = set()
        for i in range(n-2):
            left = i+1
            right = n-1
            target = -nums[i]
            while left < right:
                if nums[left ]+ nums[right] == target:
                    triplets.add((nums[i], nums[left], nums[right]))
                    right -= 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    left += 1
        return [list(x) for x in triplets]

