class Solution:
    def rotateTheBox(self, box: list[list[str]]) -> list[list[str]]:
        if not box:
            return
        res = [["." for _ in range(len(box))] for _ in range(len(box[0]))]
        for col in range(len(box)):
            bottom = len(box[0]) - 1
            for row in reversed(range(len(box[0]))):
                if box[col][row] == "*":
                    bottom = row - 1
                if box[col][row] == "#":
                    if bottom > row:
                        box[col][bottom], box[col][row] = box[col][row], box[col][bottom]
                    bottom -= 1
        res = [[box[col][row]
                for col in reversed(range(len(box)))] for row in range(len(box[0]))]
        return res


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
