class DetectSquares:

    def __init__(self):
        self.x = {}
        self.y = {}

    def add(self, point: list[int]) -> None:
        print(point)
        x, y = point[0], point[1]
        if x in self.x:
            if y in self.x[x]:
                self.x[x][y] += 1
            else:
                self.x[x][y] = 1
        else:
            self.x[x] = {y: 1}
        print(self.x)

        if y in self.y:
            if x in self.y[y]:
                self.y[y][x] += 1
            else:
                self.y[y][x] = 1
        else:
            self.y[y] = {x: 1}
        print(self.y)

    def count(self, point: list[int]) -> int:
        x, y = point[0], point[1]
        if x not in self.x or y not in self.y:
            return 0
        xArr = self.x[x]
        yArr = self.y[y]



commands = ["DetectSquares","add","add","add","count","count","add","count"]
input = [[],[[3,10]],[[11,2]],[[3,2]],[[11,10]],[[14,8]],[[11,2]],[[11,10]]] 


# Your DetectSquares object will be instantiated and called as such:
obj = DetectSquares()
for i in range(1, len(commands)):
    if commands[i] == "add":
        obj.add(input[i][0])
    else:
        obj.count(input[i][0])
