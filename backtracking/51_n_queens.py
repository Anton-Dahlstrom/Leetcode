
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
        queen_coords =[]
        final_res = []

        def PlaceQueen(n, queen_count):
            if queen_count >= n:
                print(len(x_taken))
                print(queen_count, n)
                temp = []
                for y in range(n):
                    row = ""
                    for x in range(n):
                        if (y, x) in queen_coords:
                            row += "Q"
                        else:
                            row += "."
                    temp.append(row)
                final_res.append(temp)
                return
            for y in range(n):
                if y in y_taken:
                    continue
                for x in range(n):
                    if x in x_taken:
                        continue
                    smallest = min(y ,x)
                    tempy = y - smallest
                    tempx = x - smallest

                    sub = min(y, (n-x))
                    tempy2 = y - sub
                    tempx2 = x + sub

                    if (tempy, tempx) in y_x_taken or (tempy2 ,tempx2) in y_x_taken:
                        continue
                    print(len(y_x_taken))
                    y_taken.append(y)        
                    x_taken.append(x)        
                    y_x_taken.append((tempy, tempx))        
                    y_x_taken.append((tempy2, tempx2))
                    queen_count += 1
                    queen_coords.append((y, x))
                    PlaceQueen(n, queen_count)
                    y_taken.pop()
                    x_taken.pop()
                    y_x_taken.pop()
                    y_x_taken.pop()
                    queen_coords.pop()
                    queen_count -= 1

        PlaceQueen(n, 0)
        return final_res

obj = Solution()
sol = obj.solveNQueens(4)
print(sol)
def Printer(array):
    for s in array:
        print(s)
    print("------")