class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        temp = []
        res = []
        keys = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        def dfs(i: int):
            if i == len(digits):
                res.append("".join(temp))
                return

            for ch in keys[digits[i]]:
                temp.append(ch)
                dfs(i+1)
                temp.pop()

        if not digits:
            return []
        else:
            dfs(0)
            return res