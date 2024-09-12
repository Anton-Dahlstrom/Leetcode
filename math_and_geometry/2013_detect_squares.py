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
        # print(x, y)
        # print(self.x)
        # print(self.y)
        if x not in self.x or y not in self.y:
            return 0
        res = 0
        xcopy = self.x.copy()
        ycopy = self.y.copy()
        for ykey in self.x[x]:
            for xkey in self.y[y]:
                if xkey in self.y[ykey] and abs(y-ykey) == abs(x-xkey):
                    print(x, y, xkey, ykey)
                    print(f"[[{x}, {y}], [{x}, {ykey}], [{xkey}, {y}], [{xkey}, {ykey}], ")
                    temp = 1
                    temp *= self.x[x][ykey]
                    temp *= self.y[y][xkey]
                    temp *= self.y[ykey][xkey]
                    res += temp
        self.x = xcopy
        self.y = ycopy
        return res

commands = ["DetectSquares","add","add","add","count","count","add","count"]
input = [[],[[3,10]],[[11,2]],[[3,2]],[[11,10]],[[14,8]],[[11,2]],[[11,10]]] 

# commands = ["DetectSquares","add","add","add","count"]
# input = [[],[[3,10]],[[11,2]],[[3,2]],[[11,10]]] 

commands = ["DetectSquares","add","add","add","count","add","add","add","count","add","add","add","count","add","add","add","count"]
input = [[],[[5,10]],[[10,5]],[[10,10]],[[5,5]],[[3,0]],[[8,0]],[[8,5]],[[3,5]],[[9,0]],[[9,8]],[[1,8]],[[1,0]],[[0,0]],[[8,0]],[[8,8]],[[0,8]]]

# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
for i in range(1, len(commands)):
    if commands[i] == "add":
        obj.add(input[i][0])
    else:
        print(obj.count(input[i][0]))
