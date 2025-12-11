class Solution:
    def countCoveredBuildings(self, n: int, buildings: list[list[int]]) -> int:
        minRowInCol, maxRowInCol = {}, {}
        minColInRow, maxColInRow = {}, {}
        for row, col in buildings:
            minRowInCol[col] = min(minRowInCol.get(col, float("inf")), row)
            maxRowInCol[col] = max(maxRowInCol.get(col, 0), row)

            minColInRow[row] = min(minColInRow.get(row, float("inf")), col)
            maxColInRow[row] = max(maxColInRow.get(row, 0), col)

        res = 0
        for row, col in buildings:
            if minRowInCol[col] < row and maxRowInCol[col] > row \
                    and minColInRow[row] < col and maxColInRow[row] > col:
                res += 1
        return res


n = 5
buildings = [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]]
output = 1


obj = Solution()
res = obj.countCoveredBuildings(n, buildings)
print(res)
print(output)
print(res == output)
