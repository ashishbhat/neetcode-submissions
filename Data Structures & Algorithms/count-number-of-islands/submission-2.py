class Solution:
    def search(self, grid: List[List[str]], i: int, j: int) -> None:
        if i < 0 or i > len(grid)-1 or j < 0 or j > len(grid[0]) - 1:
            return
        if grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.search(grid, i, j+1)
        self.search(grid, i, j-1)
        self.search(grid, i-1, j)
        self.search(grid, i+1, j)
        return
    def numIslands(self, grid: List[List[str]]) -> int:
        R = len(grid)
        C = len(grid[0])
        count = 0
        for r in range(0,R):
            for c in range(0,C):
                if grid[r][c] == "0":
                    continue
                self.search(grid, r, c)
                count += 1
        return count
                