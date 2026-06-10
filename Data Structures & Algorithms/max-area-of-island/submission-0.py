class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = [[False] * C for _ in range(R)]
        max_area = 0

        #1. add each valid(not 0 and not visited) element to queue
        #2. perform graph traversal from that point.
        #3. return and increment the num_islands

        def traverse(i: int, j: int) -> int:
            area  = 0
            queue = deque()
            queue.append((i,j))
            while queue:

                r,c = queue.popleft()

                if r == R or r < 0 or c == C or c < 0:
                    continue
                if visited[r][c] or grid[r][c] == 0:
                    continue

                area += 1
                visited[r][c] = True 
                queue.append((r,c+1))
                queue.append((r,c-1))
                queue.append((r - 1,c))
                queue.append((r + 1,c))
            return area


        for i in range(R):
            for j in range(C):
                if grid[i][j] == 1 and not visited[i][j]:
                    max_area = max(max_area, traverse(i,j))

        return max_area