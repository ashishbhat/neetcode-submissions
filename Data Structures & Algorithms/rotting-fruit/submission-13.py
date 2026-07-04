from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
        time_taken = 0
        while queue:
            n = len(queue)
            for _ in range(n):
                i, j = queue.popleft()
                neighbours = [(i, j+1), (i, j-1), (i-1, j), (i+1,j)]
                for i, j in neighbours:
                    if  (i >= 0 and i < len(grid) 
                        and j >= 0 and j < len(grid[0]) 
                        and grid[i][j] == 1
                    ):
                        grid[i][j] = 2;
                        queue.append((i,j))
            if queue:
                time_taken += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return time_taken
