class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        cols = {}
        rows = {}
        squares = {}

        free_squares = {}

        for row in range(len(board)):
            rows[row] = set()
            for col in range(len(board[0])):
                if not col in cols:
                    cols[col] = set()
                square = (row//3, col//3)
                if square not in squares:
                    squares[square] = set()
                    free_squares[square] = set()
                if board[row][col] != ".":
                    num = int(board[row][col])
                    rows[row].add(num)
                    cols[col].add(num)
                    squares[square].add(num)
                else:
                    free_squares[square].add((row, col))

        while free_squares:
            for num in range(1, 10):
                for key in free_squares:
                    if num in squares[key]:
                        continue
                    free_coords = free_squares[key]
                    size = len(free_coords)
                    eliminated = set()
                    # failures = 0
                    for row, col in free_coords:
                        if num in rows[row] or num in cols[col]:
                            eliminated.add((row, col))
                        # Optimization for when it works:
                        # else:
                        #     failures += 1
                        # if failures > 1:
                        #     break
                    if len(eliminated) == size - 1:
                        coord = free_coords.difference(
                            eliminated).pop()
                        board[coord[0]][coord[1]] = str(num)
                        free_squares[key].remove(coord)
                        if len(free_squares[key]) == 0:
                            free_squares.pop(key)
                        squares[key].add(num)
                        if key == (2, 0) and num == 2:
                            print(coord)
                        rows[coord[0]].add(num)
                        cols[coord[1]].add(num)
                        for b in board:
                            print(b)
                        print("----------")
                        break


board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."], [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"], ["4", ".", ".", "8",
                                                                                                                                                                                                      ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"], [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"], [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

output = [["5", "3", "4", "6", "7", "8", "9", "1", "2"], ["6", "7", "2", "1", "9", "5", "3", "4", "8"], ["1", "9", "8", "3", "4", "2", "5", "6", "7"], ["8", "5", "9", "7", "6", "1", "4", "2", "3"], ["4", "2", "6", "8",
                                                                                                                                                                                                       "5", "3", "7", "9", "1"], ["7", "1", "3", "9", "2", "4", "8", "5", "6"], ["9", "6", "1", "5", "3", "7", "2", "8", "4"], ["2", "8", "7", "4", "1", "9", "6", "3", "5"], ["3", "4", "5", "2", "8", "6", "1", "7", "9"]]
obj = Solution()

board = [[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."], [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."], [".", "6", "4", ".",
                                                                                                                                                                                                      "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."], [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"], [".", ".", ".", "2", "7", "5", "9", ".", "."]]

output = [["5", "1", "9", "7", "4", "8", "6", "3", "2"], ["7", "8", "3", "6", "5", "2", "4", "1", "9"], ["4", "2", "6", "1", "3", "9", "8", "7", "5"], ["3", "5", "7", "9", "8", "6", "2", "4", "1"], ["2", "6", "4", "3",
                                                                                                                                                                                                       "1", "7", "5", "9", "8"], ["1", "9", "8", "5", "2", "4", "3", "6", "7"], ["9", "7", "5", "8", "6", "3", "1", "2", "4"], ["8", "3", "2", "4", "9", "1", "7", "5", "6"], ["6", "4", "1", "2", "7", "5", "9", "8", "3"]]

obj.solveSudoku(board)
print(board == output)

for b in output:
    print(b)
