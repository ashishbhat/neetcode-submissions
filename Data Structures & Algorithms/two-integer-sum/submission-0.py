class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = dict()

        for i in range(len(nums)):
            if target - nums[i] in map:
                if i > map[target - nums[i]]:
                    return [map[target - nums[i]], i]
                else:
                    return [i, map[target - nums[i]]]
            else:
                map[nums[i]] = i
        
        return []
