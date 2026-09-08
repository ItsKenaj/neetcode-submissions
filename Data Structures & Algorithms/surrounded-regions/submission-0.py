class Solution:
    def solve(self, board: List[List[str]]) -> None:
        border_touching = []
        ROWS, COLS = len(board), len(board[0])

        for r in range(ROWS):
            if board[r][0] == 'O':
                border_touching.append([r, 0])
            if board[r][COLS-1] == 'O':
                border_touching.append([r, COLS-1])

        for c in range(COLS):
            if board[0][c] == 'O':
                border_touching.append([0, c])
            if board[ROWS-1][c] == 'O':
                border_touching.append([ROWS-1, c])
        

        directions = [[1,0], [0,1], [-1,0], [0,-1]]

        def dfs(stack, grid):
            while stack:
                r, c = stack.pop()
                grid[r][c] = '.'
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (0 <= row < ROWS and 0 <= col < COLS and grid[row][col] == 'O'):
                        stack.append([row, col])
        
        dfs(border_touching, board)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '.':
                    board[r][c] = 'O'