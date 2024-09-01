class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        left, right = 0, len(matrix[0])
        up, down = 0, len(matrix)
        res = []
        while True:
            if left >= right:
                break
            for i in range(left, right):
                res.append(matrix[up][i])
            up += 1

            if up >= down:
                break
            for i in range(up, down):
                res.append(matrix[i][right-1])
            right -= 1

            if left >= right:
                break
            for i in reversed(range(left, right)):
                res.append(matrix[down-1][i])
            down -= 1

            if up >= down:
                break
            for i in reversed(range(up, down)):
                res.append(matrix[i][left])
            left += 1

        return res


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16],
          [17, 18, 19, 20],
          [21, 22, 23, 24]]
output = [1, 2, 3, 4, 8, 12, 16, 20, 24, 23, 22, 21,
          17, 13, 9, 5, 6, 7, 11, 15, 19, 18, 14, 10]


obj = Solution()
res = obj.spiralOrder(matrix)
print(res)
print(output)
print(res == output)
