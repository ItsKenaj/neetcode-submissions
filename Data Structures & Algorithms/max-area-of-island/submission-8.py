from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()

        def bfs(i, j):
            area = 0
            queue = deque([(i, j)])
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            while queue:
                x, y = queue.popleft()
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                    continue
                
                if (x, y) in visited:
                    continue
                
                visited.add((x, y))
                if not grid[x][y]:
                    continue
                
                area += 1
                for dx, dy in directions:
                    queue.append((dx + x, dy + y))

            return area


        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j]:
                    max_area = max(bfs(i, j), max_area)
                
                visited.add((i, j))

        
        return max_area