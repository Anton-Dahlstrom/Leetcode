class DetectSquares:

    def __init__(self):
        self.points = {}
        self.x = {}
        self.y = {}

    def add(self, point: list[int]) -> None:
        hashpoint = tuple(point)
        print(hashpoint)
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
        print(point)
        if x not in self.x or y not in self.y:
            return 0
        res = 0
        # [11, 10]
        # [11, 2], [3, 10]
        # [3, 2]
        # self.x[x] = 2
        # self.y[y] = 3
        # self.x[self.y[y]] = 2, 10
        # self.y[self.x[x]] = 11, 3
        for key in self.x[x]:
            if key in self.y and x in self.y[key]:
                # self.x[x][key] = x 11:2
                # self.y[key][x] = y 2:11
                # self.y[y][?] = y 10:3
                # self.x[?][y] = y 3:10
                # total = self.x[x][key] + self.y[key][x] + self.x[x][y] + self.y[y][x]
                # self.y[y]
                # print(total)
                res += min(self.x[x][key], self.y[key][x])

        print(self.x)
        print(self.y)
        return res

commands = ["DetectSquares","add","add","add","count","count","add","count"]
input = [[],[[3,10]],[[11,2]],[[3,2]],[[11,10]],[[14,8]],[[11,2]],[[11,10]]] 

commands = ["DetectSquares","add","add","add","count"]
input = [[],[[3,10]],[[11,2]],[[3,2]],[[11,10]]] 

# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
for i in range(1, len(commands)):
    if commands[i] == "add":
        obj.add(input[i][0])
    else:
        print(obj.count(input[i][0]))
