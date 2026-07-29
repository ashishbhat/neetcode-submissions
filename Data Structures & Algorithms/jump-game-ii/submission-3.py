class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = len(nums) - 1
        jumps = 0
        while goal > 0:
            temp = goal
            for j in range(goal-1, -1, -1):
                if nums[j] + j >= goal:
                    temp = j
            goal = temp
            jumps += 1
        return jumps
