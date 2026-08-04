from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        def bfs(x, y):
            queue = deque([(x, y)])
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            while queue:
                cur_x, cur_y = queue.popleft()
                if cur_x < 0 or cur_x >= len(grid) or cur_y < 0 or cur_y >= len(grid[0]):
                    continue
                if (cur_x, cur_y) in visited:
                    continue
                
                visited.add((cur_x, cur_y))
                if grid[cur_x][cur_y] == "0":
                    continue
                
                for dx, dy in directions:
                    queue.append((cur_x + dx, cur_y + dy))


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if (i, j) in visited:
                    continue
                
                if grid[i][j] == "1":
                    bfs(i, j)
                    islands += 1
                visited.add((i, j))

        return islands
