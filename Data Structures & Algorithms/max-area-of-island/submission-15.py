from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0
        visited = set()
        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def bfs(r, c):
            area = 1
            queue = deque([[r, c]])
            visited.add((r, c))

            while queue:
                row, col = queue.popleft()
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        if grid[nr][nc]:
                            area += 1
                            queue.append([nr, nc])
            
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visited:
                    if grid[r][c]:
                        maxArea = max(bfs(r, c), maxArea)


        return maxArea