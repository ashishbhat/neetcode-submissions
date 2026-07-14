class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer = nums[0]
        current_ending = nums[0]
        for i in range(1, len(nums)):
            current_ending = max(
                current_ending + nums[i],
                nums[i]
            )
            answer = max(answer, current_ending)
        return answer
    
