class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        k = k + 1
        window = set()
        for i in range(len(nums)):
            if len(window) == k:
                window.remove(nums[i - k])
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False