class Solution:
    def highestPeak(self, isWater: list[list[int]]) -> list[list[int]]:
        arr = []
        starts = set()
        for r in range(len(isWater)):
            for c in range(len(isWater[0])):
                if isWater[r][c] == 1:
                    arr.append((r, c))
                    starts.add((r, c))
                    isWater[r][c] = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def isValid(r, c):
            if r not in range(len(isWater)) or c not in range(len(isWater[0])):
                return False
            return True
        height = 1
        while arr:
            temp = []
            for coord in arr:
                r, c = coord
                for dir in directions:
                    newr, newc = dir
                    newr += r
                    newc += c
                    if isValid(newr, newc) and isWater[newr][newc] == 0 and (newr, newc) not in starts:
                        isWater[newr][newc] = height
                        temp.append((newr, newc))
            arr = temp
            height += 1
        return isWater


isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
output = [[1, 1, 0], [0, 1, 1], [1, 2, 2]]

obj = Solution()
res = obj.highestPeak(isWater)
print(res)
print(output)
print(res == output)
