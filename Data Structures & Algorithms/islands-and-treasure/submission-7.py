class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        C = len(grid[0])

        def find_treasure(i: int, j: int, dist: int):
            if grid[i][j] == 0 or grid[i][j] == -1:
                return
            if 1 + dist > grid[i][j]:
                return
            grid[i][j] = min(grid[i][j] ,1 + dist)
            print(f'grid[{i}][{j}] = {grid[i][j]}')
            possible_coords = [ (i+1, j), (i - 1, j), (i, j+1), (i, j-1)]
            for coords in possible_coords:
                r,c = coords
                if r < R and r >= 0 and c < C and c >= 0:
                    find_treasure(r, c, grid[i][j])

        for i in range(R):
            for j in range(C):
                if grid[i][j] == 0:
                    possible_coords = [ (i+1, j), (i - 1, j), (i, j+1), (i, j-1)]
                    for coords in possible_coords:
                        r,c = coords
                        if r < R and r >= 0 and c < C and c >= 0:
                            find_treasure(r, c, 0)
        return