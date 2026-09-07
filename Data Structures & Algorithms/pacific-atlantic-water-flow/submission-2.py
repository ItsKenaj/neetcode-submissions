from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        reaches_pac = [[False] * COLS for _ in range(ROWS)]
        reaches_atl = [[False] * COLS for _ in range(ROWS)]

        pacific, atlantic = [], []
        for r in range(ROWS):
            pacific.append([r, 0])
            atlantic.append([r, COLS-1])
        
        for c in range(COLS):
            pacific.append([0, c])
            atlantic.append([ROWS-1, c])

        
        directions = [[1,0], [0,1], [-1,0], [0,-1]]
        def bfs(source, ocean):
            queue = deque(source)
            while queue:
                r, c = queue.popleft()
                ocean[r][c] = True
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (0 <= row < ROWS and 0 <= col < COLS and not ocean[row][col] and heights[row][col] >= heights[r][c]):
                        queue.append([row, col])

        bfs(pacific, reaches_pac)
        bfs(atlantic, reaches_atl)

        reaches_both = []
        for r in range(ROWS):
            for c in range(COLS):
                if reaches_pac[r][c] and reaches_atl[r][c]:
                    reaches_both.append([r, c])
        
        return reaches_both

