from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        
        def bfs(x, y):
            area = 0
            queue = deque([(x, y)])
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            while queue:
                curr_x, curr_y = queue.popleft()
                if curr_x < 0 or curr_x >= len(grid) or curr_y < 0 or curr_y >= len(grid[0]):
                    continue
                if (curr_x, curr_y) in visited:
                    continue
                
                visited.add((curr_x, curr_y))
                if not grid[curr_x][curr_y]:
                    continue
                area += 1

                for dx, dy in directions:
                    queue.append((curr_x + dx, curr_y + dy))

            return area
                
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue

                if grid[i][j] == 1:
                    max_area = max(bfs(i, j), max_area)
                
                visited.add((i, j))
            
        return max_area