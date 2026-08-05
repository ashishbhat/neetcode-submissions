class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        ROWS, COLS = len(matrix), len(matrix[0])
        answer = 0

        def dfs(r: int, c: int) -> int:
            if (r, c) in dp:
                return dp[(r, c)]
            
            res = 0
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < ROWS and 0 <= nc < COLS and matrix[nr][nc] > matrix[r][c]:
                    res = max(res, dfs(nr, nc))
            dp[(r, c)] = res + 1
            return dp[(r, c)]

        for i in range(ROWS):
            for j in range(COLS):
                answer = max(answer, dfs(i, j))
        print(dp)
        
        return answer
        