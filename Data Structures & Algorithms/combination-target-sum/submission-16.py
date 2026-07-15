class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(arr: list[int], index = 0 , total = 0, sequence = []) -> None:
            #print(total, target)
            results
            if index == len(arr) or total > target:
                return
            if total == target:
                results.append(sequence.copy())
                return

            if total + arr[index] <= target:
                sequence.append(arr[index])
                backtrack(arr, index, total + arr[index], sequence)
            else:
                sequence.append(arr[index])
                backtrack(arr, index + 1, total + arr[index], sequence)

            sequence.pop()
            backtrack(arr, index + 1, total, sequence)
            

        backtrack(nums, 0, 0, [])
        return results