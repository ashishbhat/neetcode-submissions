from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: [int, set] = defaultdict(set)
        columns: [int, set] = defaultdict(set)
        cells: [int, set] = defaultdict(set)

        R = len(board)
        C = len(board[0])

        for i in range(R):
            for j in range(C):
                val = board[i][j]
                if val == '.':
                    continue

                if val in rows[i]:
                    return False
                else:
                    rows[i].add(val)

                if val in columns[j]:
                    return False
                else:
                    columns[j].add(val)
                
                cell_id = 3*(i//3) + (j//3)
                if val in cells[cell_id]:
                    return False
                else:
                    cells[cell_id].add(val)
        return True





        