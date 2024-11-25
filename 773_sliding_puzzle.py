class Solution:
    def slidingPuzzle(self, board: list[list[int]]) -> int:
        self.goal = "123450"
        visited = {}
        self.res = float("inf")

        def backtracking(board, row, col, count):
            if count >= self.res:
                return
            state = "".join([str(n) for row in board for n in row])
            if state == self.goal:
                self.res = min(self.res, count)
                return
            count += 1

            if state in visited:
                if count < visited[state]:
                    visited[state] = count
                else:
                    return
            visited[state] = count

            newRow = 1 - row
            board[row][col], board[newRow][col] = board[newRow][col], board[row][col]
            backtracking(board, newRow, col, count)
            board[row][col], board[newRow][col] = board[newRow][col], board[row][col]

            for newCol in range(max(col-1, 0), min(col+1, len(board[0])-1)+1):
                if newCol == col:
                    continue
                board[row][newCol], board[row][col] = board[row][col], board[row][newCol]
                backtracking(board, row, newCol, count)
                board[row][newCol], board[row][col] = board[row][col], board[row][newCol]

        for row in range(0, len(board)):
            for col in range(0, len(board[0])):
                if board[row][col] == 0:
                    backtracking(board, row, col, 0)
                    break
        if self.res == float("inf"):
            return -1
        return self.res


board = [[4, 1, 2], [5, 0, 3]]
output = 5

obj = Solution()
res = obj.slidingPuzzle(board)
print(res)
print(output)
print(res == output)
