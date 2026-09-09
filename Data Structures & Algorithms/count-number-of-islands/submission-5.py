from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        visited = set()


        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        def bfs(r, c):
            queue = deque([[r,c]])
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS 
                    and 0 <= nc < COLS 
                    and grid[nr][nc] == '1'
                    and  (nr, nc) not in visited):
                        queue.append([nr, nc])
                        visited.add((nr, nc))

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited and grid[r][c] == '1':
                        bfs(r, c)
                        islands += 1

        return islands