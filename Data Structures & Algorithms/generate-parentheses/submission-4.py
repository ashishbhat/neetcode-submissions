class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(i: int, n: int, current, openn, close):
            if i == 2*n:
                result.append(current)
                return

            if openn < n:
                backtrack(i+1, n, current+"(", openn + 1, close)

            if close < openn:
                backtrack(i+1, n, current+")", openn, close + 1)
    
        backtrack(0, n, "", 0, 0)
        return result