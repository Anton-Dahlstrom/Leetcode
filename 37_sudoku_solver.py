class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        cols = {}
        rows = {}
        squares = {}

        free_cols = {}
        free_rows = {}
        free_squares = {}

        for row in range(len(board)):
            rows[row] = set()
            free_rows[row] = set()
            for col in range(len(board[0])):
                if not col in cols:
                    cols[col] = set()
                    free_cols[col] = set()
                square = (row//3, col//3)
                if square not in squares:
                    squares[square] = set()
                    free_squares[square] = set()
                if board[row][col] != ".":
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    squares[square].add(board[row][col])
                else:
                    free_rows[row].add((row,col))
                    free_cols[col].add((row,col))
                    free_squares[square].add((row,col))

        while free_squares:
            for key, free_coords in free_squares:
                for num in range(11):
                    if num in squares[key]:
                        continue
                    for row, col in key:
                            if num in rows[row] or num in cols[col]:
                                continue
                    free_copy = free_coords.copy()
                    free_count = len(free_copy)
                    # while free_count > 1:


board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

output = [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
obj = Solution()

obj.solveSudoku(board)
# print(board)
# print(output)