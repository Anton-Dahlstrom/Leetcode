class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        spiral = [[0 for _ in range(n)] for _ in  range(n)]
        curNum = 1
        left, right, top, bottom = 0, n, 0, n
        while left < right:
            for i in range(left, right):
                spiral[top][i] = curNum
                curNum += 1
            top += 1

            for i in range(top, bottom):
                spiral[i][right-1] = curNum
                curNum += 1
            right -= 1

            for i in reversed(range(left, right)):
                spiral[bottom-1][i] = curNum
                curNum += 1
            bottom -= 1

            print(top, bottom)
            for i in reversed(range(1,2)):
                print(i)

            for i in reversed(range(top, bottom)):
                print(i)
                spiral[i][left] = curNum
                curNum += 1
            left += 1
                
        return spiral
    

n = 3
output = [[1,2,3],[8,9,4],[7,6,5]]

obj = Solution()
res = obj.generateMatrix(n)
print(res)
print(output)
print(res == output)