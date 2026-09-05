from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def bfs(i, j):
            directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                    continue
                
                if (x, y) in visited:
                    continue

                visited.add((x, y))
                if grid[x][y] == "0":
                    continue
                
                for dx, dy in directions:
                    queue.append((dx + x, dy + y))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue

                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
                visited.add((i, j))

        return islands