class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_fruits = 0
        R = len(grid)
        C = len(grid[0])
        queue = deque()
        time = 0

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1:
                    fresh_fruits += 1
                if grid[i][j] == 2:
                    queue.append((i,j))

        
        while queue and fresh_fruits:
            time += 1
            layer_size = len(queue)

            for _ in range(layer_size):
                i, j = queue.popleft()
                for r,c in [(i+1,j), (i-1, j), (i, j + 1), (i, j - 1)]:
                    if r < R and r >= 0 and c < C and c >= 0 and grid[r][c] == 1 and fresh_fruits:
                        print(f'infected: {r},{c} at minute = {time}')
                        grid[r][c] = 2
                        queue.append((r,c))
                        fresh_fruits -= 1
        if fresh_fruits:
            return -1
        else:
            return time


        