class Solution:
    def firstCompleteIndex(self, arr: list[int], mat: list[list[int]]) -> int:
        rows = [len(mat[0])] * len(mat)
        cols = [len(mat)] * len(mat[0])
        coords = [(mat[row][col], row, col)
                  for col in range(len(mat[0])) for row in range(len(mat))]
        coords.sort()
        for i, n in enumerate(arr):
            val, row, col = coords[n-1]
            cols[col] -= 1
            if cols[col] == 0:
                return i
            rows[row] -= 1
            if rows[row] == 0:
                return i


arr = [6, 2, 3, 1, 4, 5]
mat = [[5, 1], [2, 4], [6, 3]]
output = 2

obj = Solution()
res = obj.firstCompleteIndex(arr, mat)
print(res)
print(output)
print(res == output)
