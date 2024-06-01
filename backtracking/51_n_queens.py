
# [00,01,02,03]
# [10,11,12,13]
# [20,21,22,23]
# [30,31,32,33]
# sub = min(y, n-1)-x)
# tempy = y - sub
# tempx = x + sub
# y_x_taken.append()

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        x_taken = []
        y_taken = []
        y_x_taken = []
        y_x_taken2 = []
        queen_coords =[]
        final_res = []

        def PlaceQueen(n, queen_count, level):
            if queen_count >= n:
                tempstr = ""
                temp = []
                print(temp)
                for i in range(n):
                    for j in range(n):
                        if (i, j) in queen_coords:
                            tempstr += "Q"
                        else:
                            tempstr += "."
                    temp.append(tempstr)
                    tempstr = ""
                print(temp)
                final_res.append(temp)
                return
            for y in range(level, n):
                if y in y_taken:
                    continue
                for x in range(n):
                    if x in x_taken:
                        continue
                    smallest = min(y ,x)
                    tempy = y - smallest
                    tempx = x - smallest

                    sub = min(y, ((n-1)-x))
                    tempy2 = y - sub
                    tempx2 = x + sub

                    if (tempy, tempx) in y_x_taken or (tempy2 ,tempx2) in y_x_taken2:
                        # print("START")
                        # print(y, x)
                        # print(tempy, tempx)
                        # print(y_x_taken)
                        # print(tempy2, tempx2)
                        # print(y_x_taken2)
                        # return
                        continue
                    y_taken.append(y)        
                    x_taken.append(x)        
                    y_x_taken.append((tempy, tempx))        
                    y_x_taken2.append((tempy2, tempx2))
                    queen_count += 1
                    queen_coords.append((y, x))
                    PlaceQueen(n, queen_count, y+1)
                    y_taken.pop()
                    x_taken.pop()
                    y_x_taken.pop()
                    y_x_taken2.pop()
                    queen_coords.pop()
                    queen_count -= 1
                    
        PlaceQueen(n, 0, 0)
        return final_res

obj = Solution()
sol = obj.solveNQueens(4)
print(len(sol))
def Printer(array):
    for s in array:
        print(s)
    print("------")