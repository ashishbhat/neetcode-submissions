class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []
        cols = set()
        pDiag = set()
        nDiag = set()

        def backtrack(r: int):
            if r == n:
                res.append(["".join(x) for x in board])
                return

            for c in range(n):
                if c in cols or (r-c) in nDiag or (r+c) in pDiag:
                    continue;
                cols.add(c)
                pDiag.add(r+c)
                nDiag.add(r-c)
                board[r][c] = "Q"

                backtrack(r + 1)

                cols.remove(c)
                pDiag.remove(r+c)
                nDiag.remove(r-c)
                board[r][c] = "."
    
        backtrack(0)
        return res
        

