class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(i: int, n: int, current, openn, close):
            if close > openn or openn > n:
                return

            if i == 2*n:
                result.append(current)
                return

            current += '('
            backtrack(i+1, n, current, openn + 1, close)
            current = current[:-1]

            current += ')'
            backtrack(i+1, n, current, openn, close + 1)
            current = current[:-1]
    
        backtrack(0, n, "", 0, 0)
        return result