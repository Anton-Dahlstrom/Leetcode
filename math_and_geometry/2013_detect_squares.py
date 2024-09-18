class DetectSquares:

    def __init__(self):
        self.x = {}
        self.y = {}

    def add(self, point: list[int]) -> None:
        x, y = point[0], point[1]
        if x in self.x:
            if y in self.x[x]:
                self.x[x][y] += 1
            else:
                self.x[x][y] = 1
        else:
            self.x[x] = {y: 1}

        if y in self.y:
            if x in self.y[y]:
                self.y[y][x] += 1
            else:
                self.y[y][x] = 1
        else:
            self.y[y] = {x: 1}

    def count(self, point: list[int]) -> int:
        x, y = point[0], point[1]
        if x not in self.x or y not in self.y:
            return 0
        res = 0
        for ykey in self.x[x]:
            for xkey in self.y[y]:
                if xkey in self.y[ykey] and abs(y-ykey) == abs(x-xkey) and abs(y-ykey) > 0:
                    temp = 1
                    temp *= self.x[x][ykey]
                    temp *= self.y[y][xkey]
                    temp *= self.y[ykey][xkey]
                    res += temp
        return res


commands = ["DetectSquares", "add", "add",
            "add", "count", "count", "add", "count"]
input = [[], [[3, 10]], [[11, 2]], [[3, 2]], [
    [11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
output = [1, 0, 2]
res = []

# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
for i in range(1, len(commands)):
    if commands[i] == "add":
        obj.add(input[i][0])
    else:
        count = obj.count(input[i][0])
        res.append(count)

print(res)
print(output == res)
