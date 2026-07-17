class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        N = len(word)
        ROWS, COLS = len(board), len(board[0])

        def dfs(start:  tuple[int, int], current: list[str]) -> bool:
            if len(current) == N:
                if "".join(current) == word:
                    return True
                else:
                    return False
            r, c = start
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    current.append(board[nr][nc])
                    temp = board[nr][nc]
                    board[nr][nc] = "#"
                    res = dfs((nr, nc), current)
                    current.pop()
                    board[nr][nc] = temp
                    if res == True:
                        return True
            return False

        for i in range(ROWS):
            for j in range(COLS):
                temp = board[i][j]
                board[i][j] = "#"
                if dfs((i,j), [temp]) == True:
                    return True
                board[i][j] = temp
        return False


            