from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        x_taken = {}
        y_taken = {}
        y_x_taken = {} 
        y_x_taken2 = {}
        queen_coords = {}
        final_res = []

        def PlaceQueen(n, queen_count, level):
            if queen_count >= n:
                tempstr = ""
                temp = []
                for i in range(n):
                    for j in range(n):
                        if (i, j) in queen_coords:
                            tempstr += "Q"
                        else:
                            tempstr += "."
                    temp.append(tempstr)
                    tempstr = ""
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
                        continue
                    y_taken[y] = 1       
                    x_taken[x] = 1
                    y_x_taken[(tempy, tempx)] = 1
                    y_x_taken2[(tempy2, tempx2)] = 1
                    queen_coords[(y, x)] = 1
                    queen_count += 1
                    PlaceQueen(n, queen_count, y+1)
                    y_taken.pop(y)       
                    x_taken.pop(x)
                    y_x_taken.pop((tempy, tempx))
                    y_x_taken2.pop((tempy2, tempx2))
                    queen_coords.pop((y, x))
                    queen_count -= 1
                    
        PlaceQueen(n, 0, 0)
        return final_res

# obj = Solution()
# sol = obj.solveNQueens(4)
# print(len(sol))
asd = {}
asd[2] = 1
print(asd)