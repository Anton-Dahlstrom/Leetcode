class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        rows, cols = len(box), len(box[0])
        rotated = [[box[rows - 1 - row][col]
                    for row in range(rows)] for col in range(cols)]
        rows, cols = cols, rows
        for col in range(cols):
            bottom = rows-1
            for row in range(rows-1, -1, -1):
                if rotated[row][col] == "#":
                    rotated[row][col] = "."
                    rotated[bottom][col] = "#"
                    bottom -= 1
                elif rotated[row][col] == "*":
                    bottom = row-1
        return rotated


box = [["#", ".", "*", "."],
       ["#", "#", "*", "."]]
output = [["#", "."],
          ["#", "#"],
          ["*", "*"],
          [".", "."]]

obj = Solution()
res = obj.rotateTheBox(box)
print(res)
print(output)
print(res == output)
