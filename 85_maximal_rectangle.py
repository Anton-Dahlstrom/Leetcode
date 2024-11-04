class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0

        res = 0
        for row in range(len(matrix)):
            # Checks if it's still possible to make a larger rectangle.
            if (len(matrix) - row) * len(matrix[0]) < res:
                return res
            for col in range(len(matrix[0])):
                if matrix[row][col] != "1":
                    continue
                longest = float("inf") 
                for nextRow in range(row, len(matrix)):
                    if matrix[nextRow][col] != "1":
                        break
                    temp = 0
                    for nextCol in range(col, len(matrix[0])):
                        if matrix[nextRow][nextCol] != "1":
                            break
                        temp += 1
                    longest = min(longest, temp)
                    res = max(res, longest * (1 + nextRow - row))
        return res
    
    
matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
output = 6


obj = Solution()
res = obj.maximalRectangle(matrix)
print(res)
print(output)
print(res == output)