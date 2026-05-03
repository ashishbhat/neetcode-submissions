class Solution:
    def search(self, grid: List[List[str]], i: int, j: int, visited: list ) -> int:
        if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0]) - 1:
            return 0
        if visited[i][j]:
            return 0
        visited[i][j] = True
        if grid[i][j] == "0":
            return 0
        self.search(grid, i, j+1, visited)
        self.search(grid, i, j-1, visited)
        self.search(grid, i-1, j, visited)
        self.search(grid, i+1, j, visited)
        return 1

    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        count = 0
        visited = [[False for i in range(C)] for j in range(R)]
        for r in range(0,R):
            for c in range(0,C):
                if grid[r][c] == "0" or visited[r][c]:
                    continue
                count += self.search(grid, r, c, visited)
        return count
                