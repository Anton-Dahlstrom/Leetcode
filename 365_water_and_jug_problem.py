class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        visited = set()  # xcur, ycur
        self.found = False

        def dfs(xcur, ycur, target, x, y):
            if xcur + ycur == target:
                return True
            if (xcur, ycur) in visited:
                return False
            visited.add((xcur, ycur))
            if dfs(x, ycur, target, x, y):  # fill left
                return True
            if dfs(xcur, y, target, x, y):  # fill right
                return True
            if dfs(max(0, xcur-(y-ycur)), min(y, ycur+xcur),
                   target, x, y):  # pour left to right
                return True
            if dfs(min(x, xcur+ycur), max(0, ycur - (x-xcur)),
                   target, x, y):  # pour right to left
                return True
            if dfs(0, ycur, target, x, y):  # empty left
                return True
            if dfs(xcur, 0, target, x, y):  # empty right
                return True

            return False
        return dfs(0, 0, target, x, y)


x = 3
y = 5
target = 4
# combos = 5+3, 5+1, 5+2
# combos = 2+3, 1+3, 4+3

# target - leftover, target - spill +
output = True

x = 3
y = 10
target = 4
output = True

# combos = 3+3, 3+6, 3+9
# combos = 2+10, 0+7, 0+4


obj = Solution()
res = obj.canMeasureWater(x, y, target)
print(res)
print(output)
print(res == output)
