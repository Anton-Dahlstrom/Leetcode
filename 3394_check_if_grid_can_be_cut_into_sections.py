class Solution:
    def checkValidCuts(self, n: int, rectangles: list[list[int]]) -> bool:
        m = len(rectangles)
        rectangles.sort()
        end = rectangles[0][2]
        cnt = 0
        for i in range(m):
            x1, y1, x2, y2 = rectangles[i]
            if x1 >= end:
                cnt += 1
            end = max(end, x2)
            if cnt == 2:
                return True

        rectangles.sort(key=lambda x: x[1])
        end = rectangles[0][3]
        cnt = 0
        for i in range(m):
            x1, y1, x2, y2 = rectangles[i]
            if y1 >= end:
                cnt += 1
            end = max(end, y2)
            if cnt == 2:
                return True
        return False


n = 5
rectangles = [[1, 0, 5, 2], [0, 2, 2, 4], [3, 2, 5, 3], [0, 4, 4, 5]]
output = True

n = 4
rectangles = [[0, 0, 1, 4], [1, 0, 2, 3], [
    2, 0, 3, 3], [3, 0, 4, 3], [1, 3, 4, 4]]
output = False

obj = Solution()
res = obj.checkValidCuts(n, rectangles)
print(res)
print(output)
print(res == output)
