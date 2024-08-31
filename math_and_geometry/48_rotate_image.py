class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        l, r = 0, len(matrix)-1

        while l < r:
            insideL, insideR = l, r
            while insideL < r:
                temp = matrix[l][insideL]
                matrix[l][insideL] = matrix[insideR][l]
                matrix[insideR][l] = matrix[r][insideR]
                matrix[r][insideR] = matrix[insideL][r]
                matrix[insideL][r] = temp

                insideL += 1
                insideR -= 1
            l += 1
            r -= 1
        return


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
output = [[7, 4, 1], [8, 5, 2], [9, 6, 3]]


obj = Solution()
obj.rotate(matrix)
print(matrix == output)
