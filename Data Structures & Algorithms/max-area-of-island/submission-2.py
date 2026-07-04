from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
            maxArea = 0
            rows, columns = len(grid), len(grid[0])
            visited = set()

            def calculateArea(grid: List[List[int]], i: int , j: int) -> int:
                queue = deque()
                queue.append((i,j))
                visited.add((i,j))
                area = 1

                while queue:
                    r, c = queue.popleft()
                    neighbours = [(r, c+1), (r, c-1), (r-1, c), (r+1, c)]
                    for nr, nc in neighbours:
                        if (
                            0 <= nr < rows and  
                            0 <= nc < columns and  
                            (nr, nc) not in visited and
                            grid[nr][nc] == 1
                        ):
                            queue.append((nr, nc))
                            visited.add((nr, nc))
                            area += 1
                return area
                            
            for r in range(rows):
                for c in range(columns):
                    if grid[r][c] == 1 and (r,c) not in visited:
                        maxArea = max(
                                        maxArea, 
                                        calculateArea(grid, r,c)
                                        )
            return maxArea
