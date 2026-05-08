class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        results: list[int] = [0]*n
        stack: list[int] = [0]*n

        for i in range(n):
            current_temp = temperatures[i]
            while stack and temperatures[stack[-1]] < current_temp:
                j = stack.pop()
                results[j] = i - j  
            stack.append(i)
        return results