class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(word)
        ROWS, COLS = len(board), len(board[0])

        def dfs(start:  tuple[int, int], current: list[str], visited = None) -> bool:
            if len(current) == N:
                if "".join(current) == word:
                    return True
                else:
                    return False
            r, c = start
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited:
                    current.append(board[nr][nc])
                    temp = board[nr][nc]
                    board[nr][nc] = "X"
                    res = dfs((nr, nc), current, visited)
                    current.pop()
                    board[nr][nc] = temp
                    if res == True:
                        return True
            return False

        for i in range(ROWS):
            for j in range(COLS):
                if dfs((i,j), [board[i][j]], set([(i, j)])) == True:
                    return True
        return False


            