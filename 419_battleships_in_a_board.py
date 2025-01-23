class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = set()

        def isValid(pos):
            r, c = pos
            if r in range(0, len(board)) and c in range(0, len(board[0])):
                return True
            return False

        res = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "X":
                    pos = (r, c)
                    if pos in visited:
                        continue
                    arr = [pos]
                    res += 1
                    while arr:
                        temp = []
                        for pos in arr:
                            tempr, tempc = pos
                            for direction in directions:
                                nrow, ncol = direction
                                nrow += tempr
                                ncol += tempc
                                npos = (nrow, ncol)
                                if isValid(npos) and board[nrow][ncol] == "X" and npos not in visited:
                                    visited.add(npos)
                                    temp.append(npos)
                        arr = temp
        return res


board = [["X", ".", "X", ".", "X"], [".", "X", ".", "X", "."], [".", "X", ".", ".", "."], [".", "X", ".", ".", "X"], [".", "X", ".", ".", "."], [
    "X", ".", "X", "X", "X"], [".", "X", ".", ".", "."], [".", "X", ".", "X", "."], ["X", ".", "X", ".", "X"], [".", "X", ".", ".", "X"]]
output = 14

obj = Solution()
res = obj.countBattleships(board)
print(res)
print(output)
print(res == output)
