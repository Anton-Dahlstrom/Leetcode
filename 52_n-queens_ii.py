class Solution:
    def totalNQueens(self, n: int) -> int:
        self.res = 0
        cols = set()
        downleft = set()
        downright = set()

        def placeQueen(row, cols, downleft, downright):
            if row == n:
                self.res += 1
                return
            for col in range(n):
                downl = col + row
                downr = col - row
                if col not in cols and downl not in downleft and downr not in downright:
                    cols.add(col)
                    downleft.add(downl)
                    downright.add(downr)
                    placeQueen(row+1, cols, downleft, downright)
                    cols.remove(col)
                    downleft.remove(downl)
                    downright.discard(downr)

        placeQueen(0, cols, downleft, downright)
        return self.res


n = 4
output = 2


obj = Solution()
res = obj.generateMatrix(n)
print(res)
print(output)
print(res == output)