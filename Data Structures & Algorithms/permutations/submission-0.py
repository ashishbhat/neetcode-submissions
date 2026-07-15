class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        current = set(nums)
        x = []
        def helper():
            if not current:
                result.append(x.copy())

            for i in list(current):
                current.discard(i)
                x.append(i)
                helper()
                x.pop()
                current.add(i)
        helper()
        return result