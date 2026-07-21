class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        temp = []
        res = []
        keys = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        def dfs(i: int):
            if i == len(digits):
                res.append("".join(temp))
                return

            for j in keys[digits[i]]:
                temp.append(j)
                dfs(i+1)
                temp.pop()

        if not digits:
            return []
        else:
            dfs(0)
            return res