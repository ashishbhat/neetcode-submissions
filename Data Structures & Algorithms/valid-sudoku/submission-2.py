class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        grid = set()

        n = 9

        for i in range(n):
            r = (i // 3)*3
            c = 3*(i % 3)
            for p in range(r, r+3):
                for q in range(c, c+3):
                    entry = board[p][q]
                    if entry == ".": continue
                    if entry in rows[p]:
                        return False
                    else:
                        rows[p].add(entry)

                    if entry in columns[q]:
                        return False
                    else:
                        columns[q].add(entry)

                    if entry in grid:
                        return False
                    else:
                        grid.add(entry)
            grid.clear()
        return True



        