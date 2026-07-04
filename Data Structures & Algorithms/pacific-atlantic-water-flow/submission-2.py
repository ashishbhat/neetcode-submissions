class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificSet = set()
        atlanticSet = set()

        rows = len(heights)
        columns = len(heights[0])

        for r in range(rows):
            for c in range(columns):
                if r == 0 or c == 0:
                    pacificSet.add((r,c))
                if r == rows - 1 or c == columns - 1:
                    atlanticSet.add((r,c))

        def bfs(start: set[tuple[int, int]]) -> None:
            queue = deque()
            for r, c in start:
                queue.append((r, c))
            
            while queue:
                r, c = queue.popleft()
                for nr, nc in [(r,c+1), (r, c - 1), (r - 1, c), (r + 1, c)]:
                    if (
                        0 <= nr < rows and 
                        0 <= nc < columns and 
                        heights[nr][nc] >= heights[r][c] 
                        and (nr, nc) not in start
                        ):
                            start.add((nr, nc))
                            queue.append((nr, nc))

        bfs(pacificSet)
        bfs(atlanticSet)
        return list(pacificSet.intersection(atlanticSet))
        
        
