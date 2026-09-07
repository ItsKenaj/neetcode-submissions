from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        reaches_pac = [[False] * COLS for _ in range(ROWS)]
        reaches_atl = [[False] * COLS for _ in range(ROWS)]

        pacific = []
        atlantic = []

        for c in range(COLS):
            pacific.append([0, c])
            atlantic.append([ROWS-1, c])
        
        for r in range(ROWS):
            pacific.append([r, 0])
            atlantic.append([r, COLS-1])

        def bfs(source, ocean):
            queue = deque(source)
            while queue:
                r, c = queue.popleft()
                ocean[r][c] = True

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and not ocean[nr][nc] and heights[nr][nc] >= heights[r][c]):
                        queue.append([nr, nc])
        
        bfs(pacific, reaches_pac)
        bfs(atlantic, reaches_atl)

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if reaches_pac[r][c] and reaches_atl[r][c]:
                    res.append([r, c])
        
        return res
