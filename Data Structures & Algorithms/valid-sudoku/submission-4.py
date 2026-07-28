class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = [dict() for _ in range(len(board[0]))]
        rows = [dict() for _ in range(len(board))]
        for r in range(len(board)):
            for c in range(len(board[r])):
                val = board[r][c]
                if val == ".":
                    continue

                if cols[c].get(val):
                    return False
                else:
                    cols[c][val] = 1

                if rows[r].get(val):
                    return False
                else:
                    rows[r][val] = 1


        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                sub_grid = [board[i][x:x+3] for i in range(y, y+3)]
                mini_dict = defaultdict(int)
                for row in sub_grid:
                    for val in row:
                        if val == ".":
                            continue
                        if mini_dict[val]:
                            return False
                        else:
                            mini_dict[val] = 1
        return True

            
        # cols = defaultdict(set)
        # rows = defaultdict(set)
        # squares = defaultdict(set)

        # for r in range(len(board)):
        #     for c in range(len(board[r])):
        #         val = board[r][c]
        #         if val == '.':
        #             continue

        #         if (val in cols[c] or
        #             val in rows[r] or
        #             val in squares[(r // 3, c // 3)]):
        #             return False

        #         cols[c].add(val)
        #         rows[r].add(val)
        #         squares[(r//3, c//3)].add(val)

        # return True