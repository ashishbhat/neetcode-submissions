class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = [[False] * C for _ in range(R)]
        num_islands = 0

        def explore(i: int, j: int):
            if i == R or i < 0 or j == C or j < 0:
                return
            if visited[i][j] or grid[i][j] == "0":
                return
            visited[i][j] = True
            explore(i, j+1)
            explore(i, j-1)
            explore(i - 1, j)
            explore(i + 1, j)
            return

        for i in range(R):
            for j in range(C):
                if grid[i][j] == "1" and not visited[i][j]:
                    explore(i,j)
                    num_islands += 1

        return num_islands
