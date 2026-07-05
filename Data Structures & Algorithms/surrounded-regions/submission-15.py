class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        zeros = set()
        queue = deque()

        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if board[r][c] == 'O':
                    zeros.add((r, c))

        print(zeros)


        for c in range(COLS):
            if board[0][c] == 'O':
                queue.append((0, c))
            if board[ROWS - 1][c] == 'O':
                queue.append((ROWS - 1, c))

        for r in range(ROWS):
            if board[r][0] == 'O':
                queue.append((r, 0))
            if board[r][COLS - 1] == 'O':
                queue.append((r, COLS - 1))
        print(queue)

        visited = set(queue)
        while queue:
            i, j = queue.popleft()

            for r, c in [(i+1, j), (i-1, j), (i, j+1),(i, j-1)]:
                if 0 <= r < ROWS - 1 and 0 <= c < COLS - 1 and (r,c) not in visited and board[r][c] == 'O':
                    zeros.discard((r,c))
                    queue.append((r,c))
                    visited.add((r, c))
        
        for r, c in zeros:
            board[r][c] = "X"

        


        
        
