from collections import deque
class Solution:
    INF = 2147483647
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        r , c = len(grid), len(grid[0])
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))
        
        while queue:
            i, j, dist = queue.popleft()
            neighbours = [(i, j+1), (i, j-1), (i-1, j), (i+1,j)]
            for nr, nc in neighbours:
                if (0 <= nr < r and 
                    0 <= nc < c and
                    grid[nr][nc] == Solution.INF):
                        grid[nr][nc] =  dist + 1
                        queue.append((nr,nc,dist + 1))