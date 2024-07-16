class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board:
            return
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        unchanged = set()
        lenR = len(board)
        lenC = len(board[0])
        self.save = False

        def dfs(r, c):
            if r in (0, lenR-1) or c in (0, lenC-1):
                self.save = True
            for d in directions:
                newR, newC = d
                newR += r
                newC += c
                if ((-1 < newR < lenR) and
                    (-1 < newC < lenC) and
                        ((newR, newC) not in unchanged) and
                        ((newR, newC) not in visited) and
                        board[newR][newC] == "O"):
                    visited.add((newR, newC))
                    dfs(newR, newC)

        for row in range(lenR):
            for col in range(lenC):
                if (row, col) not in unchanged and board[row][col] == "O":
                    visited = set()
                    self.save = False
                    dfs(row, col)
                    visited.add((row, col))
                    if self.save:
                        unchanged.update(visited)
                    else:
                        for coord in visited:
                            board[coord[0]][coord[1]] = "X"


board = [["X", "X", "X", "X"], ["X", "O", "O", "X"],
         ["X", "X", "O", "X"], ["X", "O", "X", "X"]]

output = [["X", "X", "X", "X"], ["X", "X", "X", "X"],
          ["X", "X", "X", "X"], ["X", "O", "X", "X"]]

board = [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"],
         ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"],
         ["X", "X", "X", "X", "O", "X", "X", "X", "X", "X"],
         ["X", "O", "X", "X", "X", "O", "X", "X", "X", "O"],
         ["O", "X", "X", "X", "O", "X", "O", "X", "O", "X"],
         ["X", "X", "O", "X", "X", "O", "O", "X", "X", "X"],
         ["O", "X", "X", "O", "O", "X", "O", "X", "X", "O"],
         ["O", "X", "X", "X", "X", "X", "O", "X", "X", "X"],
         ["X", "O", "O", "X", "X", "O", "X", "X", "O", "O"],
         ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]

output = [["X", "O", "O", "X", "X", "X", "O", "X", "O", "O"], ["X", "O", "X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X", "X", "O"], ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"], [
    "X", "X", "X", "X", "X", "X", "X", "X", "X", "X"], ["O", "X", "X", "X", "X", "X", "X", "X", "X", "O"], ["O", "X", "X", "X", "X", "X", "X", "X", "X", "X"], ["X", "X", "X", "X", "X", "X", "X", "X", "O", "O"], ["X", "X", "X", "O", "O", "X", "O", "X", "X", "O"]]

obj = Solution()
res = obj.solve(board)
for b in board:
    print(b)
print(board == output)
